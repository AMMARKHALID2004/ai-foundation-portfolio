import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/track_learning.py'
spec = importlib.util.spec_from_file_location('tracking', SCRIPT)
tracking = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tracking)


class TrackingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for folder in ('docs', 'templates', 'tracking', 'learning-inbox'):
            (self.root / folder).mkdir()
        self.progress = '# My manual tracker\n\nSupervisor: pending.\n'
        (self.root / 'docs/PROGRESS.md').write_text(self.progress)
        for name in ('reflection', 'experiment'):
            (self.root / f'templates/{name}.md').write_text(f'# My {name}\nTO FILL\n')
        (self.root / 'tracking/config.json').write_text(json.dumps({'repositories': [
            {'repository': 'AMMARKHALID2004/Numpy', 'module': 'refresh'}]}))

    def tearDown(self):
        self.temp.cleanup()

    def file(self, name, data='print(1)\n'):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(data)
        return path

    def test_baseline_new_file_changed_file_and_repeat_scan(self):
        self.file('modules/01-python-data-git/notebooks/old.py')
        tracker = tracking.Tracker(self.root)
        tracker.sync()
        self.assertEqual(tracker.events, 0)
        path = self.file('modules/01-python-data-git/notebooks/new.py')
        tracker = tracking.Tracker(self.root)
        tracker.sync()
        self.assertEqual(tracker.events, 1)
        entry = tracker.entries[0]
        self.assertIsNone(entry['learned_on'])
        self.assertEqual(entry['status'], 'File detected; review pending')
        reflection = self.root / entry['folder'] / 'reflection.md'
        reflection.write_text('My own explanation.\n')
        tracker = tracking.Tracker(self.root)
        tracker.sync()
        self.assertEqual(tracker.report()['changed_files'], [])
        path.write_text('print(2)\n')
        tracker = tracking.Tracker(self.root)
        tracker.sync()
        self.assertEqual(len(tracker.entries), 1)
        self.assertEqual(tracker.events, 1)
        self.assertEqual(reflection.read_text(), 'My own explanation.\n')
        self.assertTrue((self.root / 'docs/PROGRESS.md').read_text().startswith(self.progress))

    def test_github_baseline_then_only_changed_sources_and_failure_retry(self):
        with patch.object(tracking, 'github_files', return_value=('a'*40, {'arrays.ipynb': 'old'})):
            tracking.Tracker(self.root).sync(github=True)
        with patch.object(tracking, 'github_files', side_effect=RuntimeError('temporary API error')):
            failed = tracking.Tracker(self.root)
            failed.sync(github=True)
            self.assertEqual(len(failed.errors), 1)
        with patch.object(tracking, 'github_files', return_value=('b'*40, {'arrays.ipynb': 'new', 'other.py': 'new'})):
            tracker = tracking.Tracker(self.root)
            tracker.sync(github=True)
            self.assertEqual(tracker.events, 2)
            self.assertIn('/blob/'+'b'*40+'/', tracker.entries[0]['source']['url'])
        with patch.object(tracking, 'github_files', return_value=('b'*40, {'arrays.ipynb': 'new', 'other.py': 'new'})):
            tracker = tracking.Tracker(self.root)
            tracker.sync(github=True)
            self.assertEqual(tracker.events, 0)
            self.assertEqual(tracker.changed, [])

    def test_ambiguous_inbox_can_be_assigned_without_modifying_notebook(self):
        notebook = {'cells': [], 'metadata': {}, 'nbformat': 4, 'nbformat_minor': 5}
        path = self.file('learning-inbox/lesson.ipynb', json.dumps(notebook))
        tracker = tracking.Tracker(self.root)
        tracker.sync()
        self.assertEqual(tracker.pending, ['learning-inbox/lesson.ipynb'])
        self.assertEqual(tracker.entries, [])
        notebook['metadata']['learning_tracker'] = {'module': 'course1'}
        path.write_text(json.dumps(notebook))
        before = path.read_bytes()
        tracker = tracking.Tracker(self.root)
        tracker.sync()
        self.assertEqual(tracker.entries[0]['module'], 'course1')
        self.assertEqual(path.read_bytes(), before)

    def test_manual_note_updates_same_local_record_and_keeps_real_date(self):
        tracker = tracking.Tracker(self.root)
        entry = tracker.add('Pipeline', 'pipeline', source={'local':'practice/sklearn-pipelines/work.ipynb'}, identity='local:practice/sklearn-pipelines/work.ipynb', fingerprint='abc')
        tracker.add('Pipeline', 'pipeline', note='I fitted preprocessing inside each fold.', learned_on='2026-10-15', source={'local':'practice/sklearn-pipelines/work.ipynb'}, identity='local:practice/sklearn-pipelines/work.ipynb')
        tracker.render()
        tracker.save()
        self.assertEqual(len(tracker.entries), 1)
        self.assertEqual(entry['learned_on'], '2026-10-15')
        self.assertEqual(entry['status'], 'Reported learning')
        with self.assertRaises(ValueError):
            tracker.add('Something', None)
        with self.assertRaises(ValueError):
            tracker.add('Pipeline', 'pipeline', learned_on='2026-02-30')
        with self.assertRaises(ValueError):
            tracking.inside(self.root, '../outside.ipynb')

    def test_unknown_dates_markdown_text_and_public_repo_constraint(self):
        tracker = tracking.Tracker(self.root)
        entry = tracker.add('Topic | <script> [link]', 'refresh', note='I tried an example.\nNext: arrays.')
        tracker.render()
        self.assertIsNone(entry['learned_on'])
        rendered = (self.root / entry['folder'] / 'README.md').read_text()
        self.assertNotIn('<script>', rendered)
        with patch.object(tracking, 'gh', return_value={'private': True}):
            with self.assertRaises(ValueError):
                tracking.github_files('AMMARKHALID2004/Numpy')
        with self.assertRaises(ValueError):
            tracking.github_files('other-owner/private-repo')

    def test_unrouted_github_file_is_retried_after_explicit_assignment(self):
        config = {'repositories': [{'repository': 'AMMARKHALID2004/Machine-Learning', 'module': 'pipeline'}]}
        path = self.root / 'tracking/config.json'
        path.write_text(json.dumps(config))
        with patch.object(tracking, 'github_files', return_value=('a'*40, {})):
            tracking.Tracker(self.root).sync(github=True)
        with patch.object(tracking, 'github_files', return_value=('b'*40, {'lesson.ipynb': 'new'})):
            tracker = tracking.Tracker(self.root)
            tracker.sync(github=True)
            self.assertEqual(tracker.events, 0)
            self.assertEqual(tracker.pending, ['AMMARKHALID2004/Machine-Learning:lesson.ipynb'])
            config['file_modules'] = {'AMMARKHALID2004/Machine-Learning:lesson.ipynb': 'course1'}
            path.write_text(json.dumps(config))
            tracker = tracking.Tracker(self.root)
            tracker.sync(github=True)
            self.assertEqual(tracker.entries[0]['module'], 'course1')

    def test_manual_inbox_assignment_survives_next_scan(self):
        path = 'learning-inbox/lesson.py'
        self.file(path)
        tracker = tracking.Tracker(self.root)
        tracker.add('My linear regression', 'course1', note='I learned how the loss changes.',
                    source={'local': path}, identity=f'local:{path}')
        tracker.save()
        tracker = tracking.Tracker(self.root)
        tracker.sync()
        self.assertEqual(tracker.pending, [])
        self.assertEqual(len(tracker.entries), 1)
        self.assertEqual(tracker.entries[0]['module'], 'course1')


if __name__ == '__main__':
    unittest.main()

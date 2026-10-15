import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from update_checklist import parse_checklist, sync_checklist


class ChecklistTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for folder in ['docs', 'tracking', 'templates', 'machine-learning/preprocessing']:
            (self.root / folder).mkdir(parents=True)
        (self.root / 'docs/PROGRESS.md').write_text('# My manual progress\nSupervisor: pending.\n')
        (self.root / 'tracking/checklist-issue.json').write_text('{"url":"https://github.com/AMMARKHALID2004/ai-foundation-portfolio/issues/1"}')
        for name in ['reflection', 'experiment']:
            (self.root / f'templates/{name}.md').write_text('I add my own notes here.\n')
        (self.root / 'machine-learning/preprocessing/README.md').write_text('# My Pipeline practice\n')

    def tearDown(self):
        self.temp.cleanup()

    def test_tick_repeat_untick_and_retick_preserve_notes(self):
        body = '## ml-preprocessing — Pipeline\n\n- [x] My Pipeline exercise\n- [ ] My leakage explanation\n'
        tracker = sync_checklist(body, self.root)
        self.assertEqual(len(tracker.entries), 1)
        entry = tracker.entries[0]
        self.assertIsNone(entry['learned_on'])
        self.assertEqual(entry['status'], 'Reported complete (checklist)')
        reflection = self.root / entry['folder'] / 'reflection.md'
        reflection.write_text('My original reflection.\n')
        again = sync_checklist(body, self.root)
        self.assertEqual(again.changed, [])
        unchecked = sync_checklist(body.replace('[x]', '[ ]'), self.root)
        self.assertEqual(unchecked.entries[0]['status'], 'Not checked')
        reticked = sync_checklist(body, self.root)
        self.assertEqual(len(reticked.entries), 1)
        self.assertEqual(reticked.entries[0]['status'], 'Reported complete (checklist)')
        self.assertEqual(reflection.read_text(), 'My original reflection.\n')
        progress = (self.root / 'docs/PROGRESS.md').read_text()
        self.assertIn('Supervisor: pending.', progress)
        self.assertIn('| Preprocessing and feature engineering | 1 / 2 | 1 |', progress)

    def test_removed_topic_is_retained_with_honest_status(self):
        sync_checklist('## numpy — Libraries\n- [x] NumPy\n- [ ] Pandas\n', self.root)
        tracker = sync_checklist('## numpy — Libraries\n- [ ] Pandas\n', self.root)
        self.assertEqual(tracker.entries[0]['status'], 'Removed from checklist')

    def test_new_topic_routes_to_its_heading_and_keeps_source_link(self):
        tracker = sync_checklist('## ml-regression — Supervised ML\n- [x] [My regression](https://github.com/AMMARKHALID2004/Machine-Learning/blob/main/work.ipynb)\n', self.root)
        self.assertEqual(tracker.entries[0]['module'], 'ml-regression')
        self.assertTrue(tracker.entries[0]['folder'].startswith('machine-learning/regression/learning/'))
        self.assertTrue(tracker.entries[0]['source']['url'].endswith('/work.ipynb'))

    def test_invalid_input_does_not_write_partial_progress(self):
        for body in ['', '- [x] Missing heading', '## invalid — Other\n- [x] Wrong module',
                     '## numpy — Libraries\n- [x] NumPy\n- [x] NumPy']:
            with self.subTest(body=body):
                with self.assertRaises(ValueError):
                    sync_checklist(body, self.root)
        self.assertFalse((self.root / 'tracking/entries.json').exists())

    def test_topic_text_is_data_and_cannot_escape_record_folder(self):
        tracker = sync_checklist('## numpy — Python\n- [x] ../../file $(echo test)\n', self.root)
        self.assertTrue((self.root / tracker.entries[0]['folder']).resolve().is_relative_to(self.root))
        self.assertEqual(parse_checklist('## numpy — Python\n- [x] Test\n')[0]['topic'], 'Test')

    def test_manual_review_and_dates_survive_generated_status_updates(self):
        progress = self.root / 'docs/PROGRESS.md'
        progress.write_text('| Regression | Complete — reviewed | 2026-10-01 | 2026-10-10 | Evidence | Supervisor initials |\n'
                            '| Preprocessing and feature engineering | Not started | Unknown | Unknown | Evidence | Pending |\n')
        sync_checklist('## ml-preprocessing — Pipeline\n- [x] My Pipeline exercise\n## ml-regression — ML\n- [ ] My regression\n', self.root)
        content = progress.read_text()
        self.assertIn('Complete — reviewed | 2026-10-01 | 2026-10-10', content)
        self.assertIn('Checklist: 1/1 topics checked | Unknown | Unknown', content)


if __name__ == '__main__':
    unittest.main()

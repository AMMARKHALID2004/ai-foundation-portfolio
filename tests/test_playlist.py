import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from update_checklist import sync_checklist


class PlaylistTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for directory in ['tracking', 'docs', 'templates']:
            (self.root / directory).mkdir()
        self.catalog = json.loads((ROOT / 'tracking/campusx-playlist.json').read_text())
        (self.root / 'tracking/campusx-playlist.json').write_text(json.dumps(self.catalog))
        (self.root / 'tracking/checklist-issue.json').write_text(
            '{"url":"https://github.com/AMMARKHALID2004/ai-foundation-portfolio/issues/1"}')
        (self.root / 'docs/PROGRESS.md').write_text('My supervisor review is pending.\n')
        for name in ['reflection', 'experiment']:
            (self.root / f'templates/{name}.md').write_text('I add my own observations.\n')

    def tearDown(self):
        self.temp.cleanup()

    def body(self, through=31):
        lines = []
        for section in self.catalog['sections']:
            lines.append(f'## {section["key"]} — My section')
            for video in self.catalog['videos']:
                if video['module'] == section['key']:
                    tick = 'x' if video['position'] <= through else ' '
                    lines.append(f'- [{tick}] [{video["topic"]}]({video["url"]})')
        return '\n'.join(lines)

    def test_catalog_positions_and_notebook_links_are_complete(self):
        videos = self.catalog['videos']
        self.assertEqual([v['position'] for v in videos], list(range(1, 135)))
        self.assertEqual(len({v['video_id'] for v in videos}), 134)
        self.assertEqual(videos[30]['video_id'], 'lV_Z4HbNAx0')
        self.assertEqual(videos[31]['video_id'], 'kKWsJGKcMvo')
        for video in videos:
            sections = [s for s in self.catalog['sections']
                        if s['first'] <= video['position'] <= s['last']]
            self.assertEqual(len(sections), 1)
            self.assertEqual(video['module'], sections[0]['key'])
            for evidence in video['evidence']:
                self.assertTrue((ROOT / evidence).is_file())

    def test_tick_routes_record_updates_next_lesson_and_preserves_notes(self):
        first = sync_checklist(self.body(), self.root)
        self.assertEqual(len(first.entries), 31)
        index = self.root / 'machine-learning/README.md'
        self.assertIn('31/134 videos checked', index.read_text())
        self.assertIn('My next lesson: [video 032', index.read_text())
        self.assertEqual(sync_checklist(self.body(), self.root).changed, [])
        updated = sync_checklist(self.body(32), self.root)
        entry = next(e for e in updated.entries if e['topic'].startswith('Video 032'))
        self.assertTrue(entry['folder'].startswith('machine-learning/03-feature-engineering/learning/'))
        self.assertIsNone(entry['learned_on'])
        reflection = self.root / entry['folder'] / 'reflection.md'
        reflection.write_text('I compared quantile and uniform bin edges.\n')
        self.assertIn('My next lesson: [video 033', index.read_text())
        self.assertIn('32/134 videos checked', index.read_text())
        reverted = sync_checklist(self.body(31), self.root)
        self.assertEqual(next(e for e in reverted.entries if e['id'] == entry['id'])['status'], 'Not checked')
        self.assertEqual(reflection.read_text(), 'I compared quantile and uniform bin edges.\n')
        self.assertIn('31/134 videos checked', index.read_text())
        self.assertIn('My next lesson: [video 032', index.read_text())

    def test_video_completion_does_not_tick_independent_exercises(self):
        tracker = sync_checklist(self.body() + '\n## pipeline — Independent practice\n'
                                 '- [ ] My independent Pipeline exercise\n', self.root)
        self.assertFalse(any(e['topic'] == 'My independent Pipeline exercise' for e in tracker.entries))
        counts = json.loads((self.root / 'tracking/checklist-status.json').read_text())
        self.assertEqual(counts['modules']['pipeline'], {'complete': 0, 'total': 1})
        self.assertIn('My supervisor review is pending.', (self.root / 'docs/PROGRESS.md').read_text())


if __name__ == '__main__':
    unittest.main()

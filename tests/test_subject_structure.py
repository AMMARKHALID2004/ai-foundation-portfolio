import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from track_learning import MODULES
from update_checklist import parse_checklist, sync_checklist


class SubjectStructureTests(unittest.TestCase):
    def test_library_checks_create_records_in_their_own_library(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'tracking').mkdir()
            (root / 'tracking/checklist-issue.json').write_text(
                '{"url":"https://github.com/AMMARKHALID2004/ai-foundation-portfolio/issues/1"}')
            libraries = ['numpy', 'pandas', 'matplotlib', 'seaborn']
            body = '\n'.join(f'## {key} — My library\n- [x] My foundation' for key in libraries)
            tracker = sync_checklist(body, root)
            self.assertEqual(len(tracker.entries), 4)
            for key in libraries:
                entry = next(e for e in tracker.entries if e['module'] == key)
                self.assertTrue(entry['folder'].startswith(f'{key}/learning/'))
                self.assertIsNone(entry['learned_on'])
            self.assertEqual(sync_checklist(body, root).changed, [])

    def test_tracking_routes_are_limited_to_the_current_subjects(self):
        for folder, _ in MODULES.values():
            self.assertIn(Path(folder).parts[0],
                          {'numpy', 'pandas', 'matplotlib', 'seaborn', 'machine-learning'})
        with self.assertRaises(ValueError):
            parse_checklist('## pytorch — Later study\n- [x] Tensors\n')

    def test_imported_source_paths_and_hashes_are_preserved(self):
        manifest = json.loads((ROOT / 'docs/import-manifest.json').read_text())
        for source in manifest['repositories']:
            self.assertRegex(source['source_commit'], r'^[a-f0-9]{40}$')
            folder = (ROOT / source['destination']).resolve()
            self.assertTrue(folder.is_relative_to(ROOT))
            for row in source['files']:
                path = (folder / row['path']).resolve()
                self.assertTrue(path.is_relative_to(folder))
                self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), row['imported_sha256'])


if __name__ == '__main__':
    unittest.main()

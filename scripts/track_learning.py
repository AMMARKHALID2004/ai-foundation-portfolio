"""Record learning evidence and detect new work. Uses only the Python standard library."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import tempfile
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import quote
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
MODULES = {'numpy': ('numpy', 'NumPy'),
 'pandas': ('pandas', 'Pandas'),
 'matplotlib': ('matplotlib', 'Matplotlib'),
 'seaborn': ('seaborn', 'Seaborn'),
 'ml-foundations': ('machine-learning/foundations', 'ML foundations'),
 'ml-data': ('machine-learning/data-collection', 'Data collection'),
 'ml-cleaning': ('machine-learning/data-cleaning', 'Data cleaning'),
 'ml-eda': ('machine-learning/exploratory-data-analysis', 'Exploratory data analysis'),
 'ml-preprocessing': ('machine-learning/preprocessing', 'Preprocessing and feature engineering'),
 'ml-pca': ('machine-learning/dimensionality-reduction', 'Dimensionality reduction'),
 'ml-regression': ('machine-learning/regression', 'Regression'),
 'ml-classification': ('machine-learning/classification', 'Classification'),
 'ml-trees': ('machine-learning/decision-trees', 'Decision trees'),
 'ml-ensembles': ('machine-learning/ensembles', 'Ensemble methods'),
 'ml-clustering': ('machine-learning/clustering', 'Clustering'),
 'ml-model-selection': ('machine-learning/model-selection', 'Model selection and evaluation'),
 'ml-projects': ('machine-learning/projects', 'Independent ML projects')}
BEGIN = '<!-- learning-tracker:start -->'
END = '<!-- learning-tracker:end -->'


def now():
    return datetime.now(ZoneInfo('Asia/Karachi')).isoformat(timespec='seconds')


def read_json(path, default):
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else default


def write(path, content, changed):
    """Replace one file atomically, and avoid changing it when content is identical."""
    if path.exists() and path.read_text(encoding='utf-8') == content:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as stream:
            stream.write(content)
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)
    changed.append(path)


def save_json(path, value, changed):
    write(path, json.dumps(value, indent=2, ensure_ascii=False) + '\n', changed)


def text(value):
    # Keep user text as text in Markdown tables and links.
    return str(value).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('|', '&#124;').replace('[', '&#91;').replace(']', '&#93;').replace('\n', ' ')


def inside(root, value):
    path = (root / value).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError('The notebook must be inside this repository.')
    return path


def link(root, document, target):
    return quote(os.path.relpath(root / target, document.parent), safe='/.-_')


def infer_module(title):
    title = title.lower().replace('_', ' ').replace('-', ' ')
    rules = [
        ('numpy', r'\bnumpy\b'),
        ('pandas', r'\bpandas\b'),
        ('matplotlib', r'\bmatplotlib\b'),
        ('seaborn', r'\bseaborn\b'),
        ('ml-preprocessing', r'\bpipeline\b|column\s*transformer|normalization|standardization|encoding|encoder|imputer|preprocessing|power transformer|binning|binarization'),
        ('ml-regression', r'linear regression|gradient descent|ridge|lasso|elasticnet'),
        ('ml-classification', r'logistic regression|naive bayes|support vector|\bsvm\b|nearest neighbou?r'),
        ('ml-trees', r'decision tree'),
        ('ml-ensembles', r'random forest|boosting|stacking|bagging'),
        ('ml-clustering', r'\b(clustering|kmeans|k means|dbscan)\b'),
        ('ml-pca', r'\bpca\b|dimensionality'),
        ('ml-eda', r'\beda\b|exploratory'),
        ('ml-cleaning', r'data cleaning'),
    ]
    hits = {module for module, pattern in rules if re.search(pattern, title)}
    return hits.pop() if len(hits) == 1 else None


def local_files(root):
    found = {}
    for module, (folder, _) in MODULES.items():
        for path in (root / folder).rglob('*'):
            rel = path.relative_to(root)
            if (path.is_file() and not path.is_symlink() and path.resolve().is_relative_to(root.resolve()) and path.suffix in {'.ipynb', '.py'}
                    and not any(p in {'learning', '.ipynb_checkpoints', '__pycache__'} for p in rel.parts)):
                found[rel.as_posix()] = (module, hashlib.sha256(path.read_bytes()).hexdigest())
    for path in (root / 'learning-inbox').rglob('*'):
        if path.is_file() and not path.is_symlink() and path.resolve().is_relative_to(root.resolve()) and path.suffix in {'.ipynb', '.py'} and '.ipynb_checkpoints' not in path.parts:
            rel = path.relative_to(root).as_posix()
            module = infer_module(path.stem)
            if path.suffix == '.ipynb':
                try:
                    configured = json.loads(path.read_text()).get('metadata', {}).get('learning_tracker', {}).get('module')
                    if configured in MODULES:
                        module = configured
                except (ValueError, AttributeError):
                    pass
            found[rel] = (module, hashlib.sha256(path.read_bytes()).hexdigest())
    return found


def gh(endpoint):
    completed = subprocess.run(['gh', 'api', endpoint], capture_output=True, text=True, timeout=45)
    if completed.returncode:
        raise RuntimeError(f'GitHub request failed for {endpoint}: {completed.stderr.strip()}')
    return json.loads(completed.stdout)


def github_files(repository):
    if not re.fullmatch(r'AMMARKHALID2004/[A-Za-z0-9_.-]+', repository):
        raise ValueError('Only the configured learning repositories are supported.')
    info = gh(f'repos/{repository}')
    if info.get('private'):
        raise ValueError(f'{repository} is private; it was not indexed for publication.')
    commit = gh(f'repos/{repository}/commits/{quote(info["default_branch"], safe="")}')['sha']
    tree = gh(f'repos/{repository}/git/trees/{commit}?recursive=1')
    if tree.get('truncated'):
        raise RuntimeError(f'{repository}: incomplete file tree; retry after review.')
    files = {row['path']: row['sha'] for row in tree['tree']
             if row['type'] == 'blob' and Path(row['path']).suffix in {'.ipynb', '.py'}
             and '.ipynb_checkpoints' not in row['path'].split('/')}
    return commit, files


class Tracker:
    def __init__(self, root=ROOT):
        self.root = Path(root).resolve()
        self.entries = read_json(self.root / 'tracking/entries.json', [])
        self.state = read_json(self.root / '.learning-tracker/state.json', {'local': {}, 'github': {}, 'local_ready': False})
        self.changed = []
        self.events = 0
        self.pending = []
        self.errors = []

    def add(self, topic, module, note='', learned_on=None, source=None, identity=None, fingerprint=None):
        if module not in MODULES:
            raise ValueError('Choose a module with --module. Run modules to see the list.')
        if not topic.strip():
            raise ValueError('A topic is required.')
        if learned_on:
            datetime.strptime(learned_on, '%Y-%m-%d')
        key = identity or f'manual:{module}:{topic.strip().casefold()}:{learned_on or "unknown"}'
        ident = hashlib.sha256(key.encode()).hexdigest()[:16]
        entry = next((row for row in self.entries if row['id'] == ident), None)
        if entry and module != entry['module']:
            raise ValueError(f'This file already has a record in {entry["module"]}. Review that record before changing its module.')
        if entry and fingerprint and entry.get('fingerprint') == fingerprint:
            return entry
        if not entry:
            slug = re.sub('[^a-z0-9]+', '-', topic.lower()).strip('-')[:55] or 'learning'
            entry = {'id': ident, 'topic': topic.strip(), 'module': module,
                     'folder': f'{MODULES[module][0]}/learning/{slug}-{ident}',
                     'first_recorded': now(), 'learned_on': learned_on,
                     'note': note, 'source': source, 'status': 'Reported learning' if note else 'File detected; review pending'}
            self.entries.append(entry)
        elif not fingerprint and entry.get('note') == note and entry.get('source') == source and entry.get('learned_on') == learned_on and entry['topic'] == topic.strip():
            return entry
        else:
            if fingerprint:
                entry['status'] = 'File changed; review pending'
            if note:
                entry['note'] = note
                entry['topic'] = topic.strip()
                entry['status'] = 'Reported learning'
                entry['learned_on'] = learned_on or entry.get('learned_on')
            if source:
                entry['source'] = source
        entry['last_recorded'] = now()
        if fingerprint:
            entry['fingerprint'] = fingerprint
        self.events += 1
        folder = self.root / entry['folder']
        for name in ('reflection', 'experiment'):
            destination = folder / f'{name}.md'
            template = self.root / f'templates/{name}.md'
            if not destination.exists() and template.exists():
                write(destination, template.read_text(), self.changed)
        return entry

    def sync(self, github=False, baseline=False):
        current = local_files(self.root)
        for entry in self.entries:
            path = (entry.get('source') or {}).get('local')
            if path in current:
                current[path] = (entry['module'], current[path][1])
        ready = self.state.get('local_ready', False)
        for path, (module, fingerprint) in current.items():
            if baseline:
                continue
            if not module:
                self.pending.append(path)
                continue
            if self.state['local'].get(path) == fingerprint:
                continue
            # The first scan establishes a baseline. Inbox files are deliberate new input.
            if ready or path.startswith('learning-inbox/'):
                self.add(Path(path).stem, module, source={'local': path}, identity=f'local:{path}', fingerprint=fingerprint)
        self.state['local'] = {path: fp for path, (_, fp) in current.items()}
        # Unrouted inbox files must remain eligible when the user sets their module.
        for path, (module, _) in current.items():
            if module is None:
                self.state['local'].pop(path, None)
        self.state['local_ready'] = True
        if github:
            config = read_json(self.root / 'tracking/config.json', {'repositories': []})
            for row in config['repositories']:
                repository = row['repository']
                try:
                    commit, files = github_files(repository)
                    files = dict(files)
                    previous = self.state['github'].get(repository)
                    unresolved = []
                    if previous is not None and not baseline:
                        for path, fingerprint in files.items():
                            if previous['files'].get(path) != fingerprint:
                                module = row['module']
                                if repository.endswith('/Machine-Learning'):
                                    assigned = next((e['module'] for e in self.entries
                                                     if (e.get('source') or {}).get('repository') == repository
                                                     and e['source'].get('path') == path), None)
                                    module = config.get('file_modules', {}).get(f'{repository}:{path}') or assigned or infer_module(path)
                                    if module not in MODULES:
                                        self.pending.append(f'{repository}:{path}')
                                        unresolved.append(path)
                                        continue
                                source = {'url': f'https://github.com/{repository}/blob/{commit}/{quote(path, safe="/")}',
                                          'repository': repository, 'commit': commit, 'path': path}
                                self.add(f'{Path(path).stem} ({repository.split("/")[-1]})', module, source=source,
                                         identity=f'github:{repository}:{path}', fingerprint=fingerprint)
                    for path in unresolved:
                        if path in previous['files']:
                            files[path] = previous['files'][path]
                        else:
                            files.pop(path, None)
                    self.state['github'][repository] = {'commit': commit, 'files': files}
                except (RuntimeError, ValueError, subprocess.TimeoutExpired, OSError) as exc:
                    self.errors.append(str(exc))
        self.render()
        self.save()

    def render(self):
        log = self.root / 'docs/LEARNING_LOG.md'
        lines = ['# My learning log', '', 'This page records new files and notes. A detection date is not a study date.',
                 'My module completion and supervisor review remain in [PROGRESS.md](PROGRESS.md).', '',
                 '| Topic | Module | Status | Study date | Last recorded |', '| --- | --- | --- | --- | --- |']
        for entry in sorted(self.entries, key=lambda x: (x['last_recorded'], x['id']), reverse=True):
            document = self.root / entry['folder'] / 'README.md'
            source = entry.get('source') or {}
            if 'url' in source:
                reference = f'[Original source]({source["url"]})'
            elif source.get('local', '').startswith('learning-inbox/'):
                reference = f'My file is local in the inbox: {text(source["local"])}. It has not been published.'
            elif 'local' in source:
                reference = f'[My file]({link(self.root, document, source["local"])})'
            else:
                reference = 'I have not linked a file yet.'
            content = '\n'.join([
                f'# {text(entry["topic"])}', '',
                '> This index is generated. I add my own writing to reflection.md and experiment.md.', '',
                f'My status: **{entry["status"]}**.',
                f'My study date: **{entry.get("learned_on") or "Unknown"}**.',
                f'This record was last updated at {entry["last_recorded"]}.', '',
                '## My note', '', text(entry.get('note') or 'I have not added a learning note yet.'), '',
                '## My evidence', '', reference, '',
                'I record my results in [experiment.md](experiment.md).',
                'I record what I learned in [reflection.md](reflection.md).', '',
                'This record does not confirm module completion or supervisor review.', ''])
            write(document, content, self.changed)
            lines.append(f'| [{text(entry["topic"])}]({link(self.root, log, entry["folder"] + "/README.md")}) | {MODULES[entry["module"]][1]} | {entry["status"]} | {entry.get("learned_on") or "Unknown"} | {entry["last_recorded"][:10]} |')
        if not self.entries:
            lines.append('| No new activity recorded yet | — | — | — | — |')
        write(log, '\n'.join(lines) + '\n', self.changed)
        progress = self.root / 'docs/PROGRESS.md'
        if progress.exists():
            original = progress.read_text()
            summary = [BEGIN, '## My automatic activity record', '',
                       'This section updates from my checklist and learning records. My study dates and supervisor reviews require actual evidence.',
                       'I use [my learning log](LEARNING_LOG.md) to open each record.', '',
                       '| Module | Checked topics | Learning records |', '| --- | --- | --- |']
            checklist = read_json(self.root / 'tracking/checklist-status.json', {}).get('modules', {})
            for module, (_, title) in MODULES.items():
                count = sum(e['module'] == module for e in self.entries)
                tick = checklist.get(module)
                checked = f'{tick["complete"]} / {tick["total"]}' if tick else '—'
                summary.append(f'| {title} | {checked} | {count} |')
            summary.extend(['', END])
            block = '\n'.join(summary)
            if BEGIN in original and END in original:
                start, finish = original.index(BEGIN), original.index(END) + len(END)
                content = original[:start] + block + original[finish:]
            elif BEGIN in original or END in original:
                raise ValueError('The automatic activity markers are incomplete. Restore them before sync.')
            else:
                content = original.rstrip() + '\n\n' + block + '\n'
            write(progress, content, self.changed)
        for module, (folder, _) in MODULES.items():
            entries = [e for e in self.entries if e['module'] == module]
            if not entries:
                continue
            index = self.root / folder / 'learning/README.md'
            rows = ['# My learning records', '', 'This index updates automatically. I keep my own notes inside each record folder.', '']
            rows += [f'- [{text(e["topic"])}]({link(self.root, index, e["folder"] + "/README.md")})' for e in entries]
            write(index, '\n'.join(rows) + '\n', self.changed)
            module_readme = self.root / folder / 'README.md'
            if module_readme.exists():
                content = module_readme.read_text()
                marker = '<!-- learning-records -->'
                if marker not in content:
                    content = content.rstrip() + '\n\n' + marker + '\n## My tracked learning\n\nI open [my learning records](learning/README.md) to find new work and notes.\n'
                    write(module_readme, content, self.changed)

    def save(self):
        save_json(self.root / 'tracking/entries.json', self.entries, self.changed)
        save_json(self.root / '.learning-tracker/state.json', self.state, [])

    def report(self):
        return {'events': self.events, 'changed_files': sorted({p.relative_to(self.root).as_posix() for p in self.changed}),
                'needs_module': self.pending, 'errors': self.errors}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('modules')
    add = sub.add_parser('add')
    add.add_argument('topic')
    add.add_argument('--module', choices=MODULES)
    add.add_argument('--note', required=True, help='What I learned, in my own words.')
    add.add_argument('--date', help='Actual study date, YYYY-MM-DD. Omit if unknown.')
    add.add_argument('--notebook', help='Existing notebook or source file inside this repository.')
    for command in ('sync', 'baseline', 'watch'):
        item = sub.add_parser(command)
        item.add_argument('--github', action='store_true')
        if command == 'watch':
            item.add_argument('--seconds', type=int, default=30)
    args = parser.parse_args(argv)
    if args.command == 'modules':
        for key, (folder, title) in MODULES.items():
            print(f'{key:15} {title}: {folder}')
        return 0
    lock = ROOT / '.learning-tracker/running.lock'
    lock.parent.mkdir(parents=True, exist_ok=True)
    # An exclusive lock prevents a scheduled sync and a notebook entry from losing updates.
    import fcntl
    with lock.open('w') as stream:
        try:
            fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            parser.exit(1, 'Another tracker is running. Try again after it finishes.\n')
        if args.command == 'add':
            tracker = Tracker()
            source = None
            identity = None
            if args.notebook:
                path = inside(ROOT, args.notebook)
                if not path.is_file() or path.suffix not in {'.ipynb', '.py'}:
                    parser.error('Choose an existing .ipynb or .py file.')
                rel = path.relative_to(ROOT).as_posix()
                source = {'local': rel}
                identity = f'local:{rel}'
            try:
                tracker.add(args.topic, args.module or infer_module(args.topic), args.note, args.date, source, identity)
                tracker.render()
                tracker.save()
                print(json.dumps(tracker.report(), indent=2))
            except ValueError as exc:
                parser.error(str(exc))
        else:
            if args.command == 'watch' and args.seconds < 10:
                parser.error('--seconds must be at least 10.')
            while True:
                tracker = Tracker()
                tracker.sync(github=args.github, baseline=args.command == 'baseline')
                print(json.dumps(tracker.report(), indent=2), flush=True)
                if args.command != 'watch':
                    return 1 if tracker.errors else 0
                # Release the lock while waiting so a notebook can add a note.
                fcntl.flock(stream, fcntl.LOCK_UN)
                time.sleep(args.seconds)
                fcntl.flock(stream, fcntl.LOCK_EX)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

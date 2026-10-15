"""Turn my GitHub issue checkboxes into learning records. No AI or extra packages."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import urlsplit

from track_learning import ROOT, MODULES, Tracker, now, read_json, save_json, write


def parse_checklist(body):
    tasks = []
    module = None
    seen = set()
    for line in body.splitlines():
        if line.startswith('## '):
            module = line[3:].split()[0]
            if module not in MODULES:
                module = None
        match = re.fullmatch(r'- \[([ xX])\] (.+)', line.strip())
        if not match:
            continue
        if module is None:
            raise ValueError('Each checkbox needs a heading that starts with a valid module key.')
        label = match[2].strip()
        linked = re.fullmatch(r'\[([^\]]+)\]\((https://[^\s()]+)\)', label)
        topic, url = (linked[1], linked[2]) if linked else (label, None)
        if not topic or len(topic) > 180:
            raise ValueError('Each topic must contain 1 to 180 characters.')
        if url and (not urlsplit(url).netloc or urlsplit(url).username):
            raise ValueError('Use a normal HTTPS source link without credentials.')
        identity = f'checklist:{module}:{topic.casefold()}'
        ident = hashlib.sha256(identity.encode()).hexdigest()[:16]
        if ident in seen:
            raise ValueError(f'Duplicate topic in {module}: {topic}')
        seen.add(ident)
        tasks.append({'id': ident, 'identity': identity, 'module': module,
                      'topic': topic, 'url': url, 'checked': match[1].lower() == 'x'})
    if not tasks or len(tasks) > 200:
        raise ValueError('The checklist must contain 1 to 200 topics.')
    return tasks


def sync_checklist(body, root=ROOT):
    tasks = parse_checklist(body)  # Validate before any writes.
    tracker = Tracker(root)
    config = read_json(tracker.root / 'tracking/checklist-issue.json', {})
    issue_url = config.get('url')
    if not issue_url or not issue_url.startswith('https://github.com/'):
        raise ValueError('A GitHub checklist issue URL is required.')
    counts = {key: {'complete': 0, 'total': 0} for key in MODULES}
    active = set()
    for task in tasks:
        active.add(task['id'])
        counts[task['module']]['total'] += 1
        counts[task['module']]['complete'] += int(task['checked'])
        entry = next((e for e in tracker.entries if e['id'] == task['id']), None)
        if task['checked']:
            entry = tracker.add(task['topic'], task['module'],
                                note='I marked this topic complete in my checklist. I have not recorded its study date.',
                                source={'url': task['url'] or issue_url}, identity=task['identity'])
            entry['origin'] = 'checklist'
        if entry:
            status = 'Reported complete (checklist)' if task['checked'] else 'Not checked'
            if entry['status'] != status:
                entry['status'] = status
                entry['last_recorded'] = now()
    for entry in tracker.entries:
        if entry.get('origin') == 'checklist' and entry['id'] not in active and entry['status'] != 'Removed from checklist':
            entry['status'] = 'Removed from checklist'
            entry['last_recorded'] = now()
    save_json(tracker.root / 'tracking/checklist-status.json', {'issue': issue_url, 'modules': counts}, tracker.changed)
    write(tracker.root / 'tracking/CHECKLIST.md', body.rstrip() + '\n', tracker.changed)
    tracker.render()
    # Update topic counts without inventing study dates or supervisor approval.
    row_names = {
        'refresh': '1 Python/data/Git refresh', 'pipeline': 'Personalized Pipeline bridge',
        'course1': '2 ML Specialization Course 1', 'course2': '3 ML Specialization Course 2',
        'unsupervised': '4 Course 3 — optional', 'pytorch': '5 PyTorch Basics',
        'videos': '6 PyTorch Beginner Series', 'deep-learning': '7 Deep-learning practice',
        'evaluation': '8 Evaluation study — optional',
    }
    progress = tracker.root / 'docs/PROGRESS.md'
    if progress.exists():
        lines = progress.read_text().splitlines()
        for module, label in row_names.items():
            status = f'Checklist: {counts[module]["complete"]}/{counts[module]["total"]} topics checked'
            for index, line in enumerate(lines):
                if line.startswith(f'| {label} |'):
                    columns = line.split('|')
                    if 'reviewed' not in columns[2].lower():
                        columns[2] = f' {status} '
                        lines[index] = '|'.join(columns)
            readme = tracker.root / MODULES[module][0] / 'README.md'
            if readme.exists():
                content = readme.read_text()
                match = re.search(r'My status: \*\*(.*?)\*\*', content)
                if match and 'reviewed' not in match[1].lower():
                    content = content[:match.start(1)] + status + content[match.end(1):]
                    write(readme, content, tracker.changed)
        write(progress, '\n'.join(lines) + '\n', tracker.changed)
    tracker.save()
    return tracker


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, help='Read a local checklist instead of fetching the GitHub issue.')
    parser.add_argument('--publish', action='store_true', help='Commit generated changes and push from a clean Actions checkout.')
    args = parser.parse_args(argv)
    if args.publish:
        if subprocess.check_output(['git', 'status', '--porcelain'], cwd=ROOT, text=True).strip():
            parser.error('Publication requires a clean checkout. Existing edits are preserved.')
        if subprocess.check_output(['git', 'branch', '--show-current'], cwd=ROOT, text=True).strip() != 'main':
            parser.error('Publication is limited to main.')
    if args.input:
        body = args.input.read_text(encoding='utf-8')
    else:
        config = read_json(ROOT / 'tracking/checklist-issue.json', {})
        repository, number = config.get('repository'), config.get('number')
        if repository != 'AMMARKHALID2004/ai-foundation-portfolio' or not isinstance(number, int) or number < 1:
            parser.error('Invalid checklist repository or issue number.')
        result = subprocess.run(['gh', 'api', f'repos/{repository}/issues/{number}'],
                                check=True, capture_output=True, text=True, timeout=45)
        issue = json.loads(result.stdout)
        if issue.get('pull_request') or issue['html_url'] != config['url']:
            parser.error('The configured source must be the checklist issue.')
        body = issue.get('body') or ''
    tracker = sync_checklist(body)
    files = sorted({p.relative_to(ROOT).as_posix() for p in tracker.changed})
    if args.publish and files:
        subprocess.run(['git', 'add', '--', *files], cwd=ROOT, check=True)
        subprocess.run(['git', '-c', 'user.name=github-actions[bot]',
                        '-c', 'user.email=41898282+github-actions[bot]@users.noreply.github.com',
                        'commit', '-m', 'Update my learning checklist'], cwd=ROOT, check=True)
        subprocess.run(['git', 'push', 'origin', 'HEAD:main'], cwd=ROOT, check=True)
    print(json.dumps({'changed_files': files, 'topic_count': len(parse_checklist(body))}, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

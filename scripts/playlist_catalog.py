"""Render my verified CampusX lesson index from the current GitHub checkboxes."""
from track_learning import link, read_json, text, write


def render_playlist(tracker, tasks):
    catalog = read_json(tracker.root / 'tracking/campusx-playlist.json', None)
    if catalog is None:
        return
    by_topic = {(task['module'], task['topic']): task for task in tasks}
    entries = {(entry['module'], entry['topic']): entry for entry in tracker.entries}
    videos = catalog['videos']

    def checked(video):
        return by_topic.get((video['module'], video['topic']), {}).get('checked', False)

    complete = sum(checked(video) for video in videos)
    next_video = next((video for video in videos if not checked(video)), None)
    index = tracker.root / 'machine-learning/README.md'
    lines = ['# My machine learning playlist', '',
             f'I follow [{catalog["title"]}]({catalog["url"]}) by {catalog["creator"]}.', '',
             f'**My progress: {complete}/{len(videos)} videos checked.**', '',
             'I reported videos 1–31 complete on 2026-10-15. My actual study dates are unknown.',
             'My ticks record lesson completion. I record independent work and supervisor review separately.', '',
             'I use playlist positions, not the Day labels in video titles. This order was verified on '
             f'{catalog["verified_on"]}. The course title does not mean that it has 100 videos.', '',
             '**[Update my checklist](https://github.com/AMMARKHALID2004/ai-foundation-portfolio/issues/1).**', '']
    if next_video:
        lines += [f'**My next lesson: [video {next_video["position"]:03d} — '
                  f'{text(next_video["title"])}]({next_video["url"]}).**', '']
    else:
        lines += ['I have checked all listed lessons. I review my independent projects next.', '']
    lines += ['## My section folders', '', '| Videos | My section | Checked |', '| --- | --- | --- |']
    for section in catalog['sections']:
        group = [video for video in videos if video['module'] == section['key']]
        done = sum(checked(video) for video in group)
        document = tracker.root / section['folder'] / 'README.md'
        lines.append(f'| {section["first"]:03d}–{section["last"]:03d} | '
                     f'[{section["title"]}]({link(tracker.root, index, section["folder"] + "/README.md")}) | {done}/{len(group)} |')
        section_lines = [f'# My {section["title"].lower()}', '',
                         f'My playlist range: **{section["first"]:03d}–{section["last"]:03d}**. '
                         f'My checked lessons: **{done}/{len(group)}**.', '',
                         'I save my notebooks in `notebooks/`, my notes in `notes/`, and my results in `results/`.',
                         'I start each filename with its video number, such as `video-032-my-practice.ipynb`.',
                         'I use the FYP AI (Anaconda) kernel. I write my own explanation and identify my sources.', '',
                         'This index updates from my GitHub checklist. I keep my own writing in the folders above '
                         'or in each learning record. Linked earlier notebooks retain their source attribution.', '',
                         '| Video | Lesson | Status | My earlier related work | Learning record |',
                         '| --- | --- | --- | --- | --- |']
        for video in group:
            key = (video['module'], video['topic'])
            task = by_topic.get(key)
            status = 'Reported complete' if checked(video) else ('Not checked' if task else 'Not on checklist')
            evidence = ', '.join(f'[Notebook {n}]({link(tracker.root, document, path)})'
                                 for n, path in enumerate(video.get('evidence', []), 1)) or 'I have not linked work yet'
            entry = entries.get(key)
            record = f'[My record]({link(tracker.root, document, entry["folder"] + "/README.md")})' if entry else '—'
            section_lines.append(f'| {video["position"]:03d} | [{text(video["title"])}]({video["url"]}) | '
                                 f'{status} | {evidence} | {record} |')
        section_lines += ['', '<!-- learning-records -->', '',
                          f'I return to [my playlist index]({link(tracker.root, document, "machine-learning/README.md")}).', '']
        write(document, '\n'.join(section_lines), tracker.changed)
    lines += ['', '## How I add my next lesson', '',
              '1. I open the section for the next video.',
              '2. I create or open my notebook in its `notebooks/` folder.',
              '3. I add my own code, source links, observations, and limits.',
              '4. I restart the kernel and run my code. I save and push my work.',
              '5. I tick that video in my GitHub issue. Actions updates this index and creates a learning record.', '',
              'My next exercise scaffold is [video 032: Binning and Binarization]'
              '(03-feature-engineering/notebooks/video-032-binning-and-binarization.ipynb). '
              'It contains tasks and blank space for my work. It has no completed results.', '',
              'I keep the earlier [Pipeline exercise](../practice/sklearn-pipelines/exercise.ipynb) '
              'as optional independent practice for video 029.', '',
              '## My sources and independent projects', '',
              'The titles and video links come from the public CampusX playlist. I have not copied '
              'video transcripts, paid notes, or course solutions.',
              'I use [the instructor repository](https://github.com/campusx-official/100-days-of-machine-learning) '
              'as a reference. I keep my earlier source copies in [completed-work](../completed-work/README.md).', '',
              'I record my own regression implementations and model comparison in [projects](projects/README.md). '
              'My supervisor guide requirements remain in [the guide map](../docs/GUIDE_MAPPING.md). '
              'I have not recorded supervisor approval to replace a required course.', '',
              'I can inspect the verified titles, video IDs, section routes, and related notebook links in '
              '[the playlist manifest](../tracking/campusx-playlist.json).', '']
    write(index, '\n'.join(lines), tracker.changed)

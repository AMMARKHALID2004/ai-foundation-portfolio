# How I track new learning

I use two inputs: files I save in this portfolio and changes I push to my 14 linked learning repositories. The active **Track my AI learning** schedule in this Codex chat checks once each hour. I keep my computer on and Codex running for local checks. I can also run a check myself. [OpenAI's scheduling guide](https://learn.chatgpt.com/docs/automations?surface=app) explains this requirement.

The first scan records the existing files as a baseline. Later scans detect new and changed `.ipynb` and `.py` files. A saved file shows activity. It does not prove that I learned a topic or completed a module.

## My normal routine

1. I save my notebook in the matching module's `notebooks/` folder, or push it to a linked learning repository.
2. I let the scheduled check record the change. I can run a check now if I need it sooner.
3. I open [my learning log](LEARNING_LOG.md) to find the new record.
4. I add my measured results and reflection in that record's folder.

For a lesson with no code, I open [Track_my_learning.ipynb](../Track_my_learning.ipynb). I select **FYP AI (Anaconda)**. I enter a topic, module, and short learning note. I run the first two code cells. I add a study date only if I know it.

I can use the same form to explain a detected notebook. I enter its path in the `notebook` field. The tracker updates the same record.

## What updates automatically

- A topic folder under the matching module's `learning/` folder.
- A source link to my notebook or the exact GitHub commit.
- Blank forms for my experiment and reflection, if the forms do not exist yet.
- The module's learning index and a link from its README.
- [My learning log](LEARNING_LOG.md) and the automatic section in [PROGRESS.md](PROGRESS.md).

The tracker keeps my original notebook where I saved it. GitHub entries link to the original file. It preserves my existing notes. Repeat scans update the same record. It does not run notebook cells.

My study dates, results, module completion, and supervisor review need actual evidence. A file starts with the status **File detected; review pending**. My own note changes the entry to **Reported learning**. This topic status does not complete the full module.

## Where I save local work

| Module key | Folder |
| --- | --- |
| `refresh` | `modules/01-python-data-git/notebooks/` |
| `pipeline` | `practice/sklearn-pipelines/` |
| `course1` | `modules/02-supervised-ml/notebooks/` |
| `course2` | `modules/03-advanced-ml/notebooks/` |
| `unsupervised` | `modules/04-unsupervised-optional/notebooks/` |
| `pytorch` | `modules/05-pytorch-basics/notebooks/` |
| `videos` | `modules/06-pytorch-video-practice/notebooks/` |
| `deep-learning` | `modules/07-deep-learning-practice/notebooks/` |
| `evaluation` | `modules/08-evaluation-optional/notebooks/` |

The tracker also scans `.py` files in these module folders. It skips generated learning records and notebook checkpoints. It leaves the imported snapshots in `completed-work/` intact.

If I am unsure about a folder, I save the file in `learning-inbox/`. A clear title, such as `numpy-arrays.ipynb`, can identify its module. If the title is unclear, the tracker reports that it needs a module. I assign the module with the Jupyter form and the notebook path. Inbox files stay local until they are reviewed for publication.

## Run a check now

From my repository root, in my Anaconda environment:

```bash
python scripts/track_learning.py sync --github
```

GitHub checks use my existing `gh` login. I can check it with `gh auth status`. I run `gh auth login` if I need to sign in. Local checks work without GitHub:

```bash
python scripts/track_learning.py sync
```

For faster local checks while I study, I can keep this command open in another terminal:

```bash
python scripts/track_learning.py watch --seconds 30
```

I press Ctrl+C to stop it. The local watcher checks files every 30 seconds. The hourly check handles GitHub changes. The local watcher uses Linux or macOS file locks, as used by this workspace.

## Add a learning note from the terminal

This is an example. I replace the topic, note, and notebook path with my actual work:

```bash
python scripts/track_learning.py add "Pipeline practice" \
  --module pipeline \
  --note "I learned how to fit preprocessing inside each training fold." \
  --notebook practice/sklearn-pipelines/exercise.ipynb
```

I can add `--date YYYY-MM-DD` for a known study date. I omit `--notebook` for a lesson without a code file. I can list module keys with `python scripts/track_learning.py modules`.

## My GitHub publication

The tracker script updates local files. It does not commit or push them. The scheduled Codex check reviews new records and eligible source files, then commits and pushes the changes through Git and GitHub CLI. It keeps restricted data, credentials, and unreviewed notebook outputs local. It does not change my original repositories or publish their datasets again.

If a file needs my explanation, a module choice, or publication review, the check tells me. It stays quiet when nothing changes. It cannot detect a lesson I watch or read unless I save a file or add a note.

The repository list is in [tracking/config.json](../tracking/config.json). Its `file_modules` map can assign an unclear GitHub file to a module. The key is `AMMARKHALID2004/repository:path/to/file.ipynb`. The value is a module key such as `course1`. Unclear Machine-Learning files stay pending until they have a module.

The recorded entries are in [tracking/entries.json](../tracking/entries.json). Detection state stays in the ignored `.learning-tracker/` folder on this computer. If that state is removed, the next scan starts a new baseline. I keep it while I use automatic tracking. The hourly schedule belongs to this Codex chat; cloning the repository does not install that schedule on another computer.

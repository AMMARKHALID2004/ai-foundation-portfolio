# AI foundation portfolio

Common foundation portfolio for Muhammad Ammar Khalid's FYP preparation, following the supervisor's **AI Learning and Specialization Guide**, version 1.0 (September 2026).

## Current position

As reported on **2026-10-15**, NumPy, Pandas, Seaborn, and Matplotlib study is complete; scikit-learn study has reached **ColumnTransformer**. Existing GitHub repositories contain related notebooks. This records prior work without assuming the complete ML or PyTorch foundation is finished. Originality, reproducibility, learning reflections, and supervisor sign-off still need review.

**Start here:** [next tasks](docs/NEXT_STEPS.md), [roadmap](docs/ROADMAP.md), and [progress tracker](docs/PROGRESS.md).

## Structure

| Folder | Purpose |
| --- | --- |
| `modules/01-python-data-git` | Prior Python/data/visualization evidence and a short diagnostic |
| `modules/02-supervised-ml` | Course 1 concepts and original linear/logistic regression |
| `modules/03-advanced-ml` | Course 2 concepts and a comparison of at least three models |
| `modules/04-unsupervised-optional` | Optional Course 3 work |
| `modules/05-pytorch-basics` | Tensors, autograd, datasets, training, saving/loading |
| `modules/06-pytorch-video-practice` | Independent reproductions of the beginner series |
| `modules/07-deep-learning-practice` | Student-written MLP/CNN loops and error analysis |
| `modules/08-evaluation-optional` | Optional dedicated evaluation study; apply evaluation in projects |
| `practice/sklearn-pipelines` | Bridge from ColumnTransformer to an end-to-end ML workflow |
| `templates` | Module evidence, experiments, reflection, dataset and model cards |
| `docs` | Planning, progress, portfolio links and submission checklist |
| `blueprints` | Plans for one future specialization repo and a separate capstone |

## Setup

Use Python 3.11 or newer and work from this repository's root.

```bash
python -m venv .venv
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python practice/sklearn-pipelines/example.py
python -m jupyter lab
```

The example generates synthetic data locally and needs no downloads or API keys. Its printed score demonstrates execution only; it is not an FYP result or evidence of student completion. Open `practice/sklearn-pipelines/exercise.ipynb` to do your own extension. For only the verified example runtime, use `python -m pip install -r requirements-example-lock.txt` on Python 3.12. Verification scope is recorded in [VERIFICATION.md](docs/VERIFICATION.md).

`requirements.txt` defines the starter environment. After validating your own experiment, save the exact environment with `python -m pip freeze > requirements-lock.txt` and record the Python version. PyTorch is intentionally deferred until its module; follow the official installation selector for your hardware then.

## Evidence and working habits

For each module, provide a README with objectives and actual dates, original source/notebooks, an environment file, measured results with interpretation, and a reflection. Add a repository/folder link and supervisor review to [PROGRESS.md](docs/PROGRESS.md). Commit meaningful increments as you learn.

Existing topic repos remain linked in [GITHUB_EVIDENCE.md](docs/GITHUB_EVIDENCE.md). Do not relabel copied tutorials or generated starters as original implementations. Attribute courses and dataset sources; publish only permitted independent work. Keep restricted graded solutions, private data, credentials and API keys out of Git.

## Foundation completion gate

- [ ] Original linear and logistic regression with loss and optimization explanations.
- [ ] At least three classical ML models compared under a justified evaluation protocol.
- [ ] A PyTorch MLP and CNN with student-written training and validation loops.
- [ ] Error analysis explaining failures and proposed improvements.
- [ ] Every completed module has evidence, reproducible setup, and review.

Choose one specialization after PyTorch. Use the [blueprints](blueprints/README.md) when ready. Scaffold creation does not complete any of these gates.

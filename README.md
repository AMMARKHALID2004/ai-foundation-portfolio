# AI foundation portfolio

Common foundation portfolio for Muhammad Ammar Khalid's FYP preparation, following the supervisor's **AI Learning and Specialization Guide**, version 1.0 (September 2026).

## Current position

As reported on **2026-10-15**, NumPy, Pandas, Seaborn, and Matplotlib study is complete; scikit-learn study has reached **ColumnTransformer**. Existing GitHub repositories contain related notebooks. This records prior work without assuming the complete ML or PyTorch foundation is finished. Originality, reproducibility, learning reflections, and supervisor sign-off still need review.

**Your completed material:** [browse the imported work](completed-work/README.md).

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
| `completed-work` | Imported notebooks, Python exercises, data-handling/EDA and preprocessing work from 14 existing repositories |
| `templates` | Module evidence, experiments, reflection, dataset and model cards |
| `docs` | Planning, progress, portfolio links and submission checklist |
| `blueprints` | Plans for one future specialization repo and a separate capstone |

## Setup: Anaconda + Jupyter Notebook

The primary workflow uses **Anaconda**, **Jupyter Notebook**, and **uv**. Work from this repository's root:

```bash
conda env create -f environment.yml
conda activate fyp-ai
uv pip install -r requirements.txt
python -m ipykernel install --user --name fyp-ai --display-name "FYP AI (Anaconda)"
python scripts/fetch_learning_data.py
python -m notebook
```

The optional data-download step uses GitHub CLI to retrieve original lesson assets locally, verifies their hashes and keeps them out of Git. You can skip it for the synthetic Pipeline starter.

In Jupyter Notebook, select the **FYP AI (Anaconda)** kernel. If the environment already exists, activate it and continue from dependency installation.

**pip alternative:** replace `uv pip install -r requirements.txt` with `python -m pip install -r requirements.txt`. Both use the same dependency file. [Environment instructions](docs/ENVIRONMENT.md) also cover uv/venv and pip/venv, optional EDA libraries, and saving exact package versions.

Run `python practice/sklearn-pipelines/example.py` for the synthetic Pipeline starter. It needs no dataset downloads or API keys; its score is a teaching result, not FYP performance. Complete `practice/sklearn-pipelines/exercise.ipynb` independently. The verified smaller runtime is in `requirements-example-lock.txt` (Python 3.12). See [verification](docs/VERIFICATION.md) for the actual checks and their limits.

## Evidence and working habits

For each module, provide a README with objectives and actual dates, original source/notebooks, an environment file, measured results with interpretation, and a reflection. Add a repository/folder link and supervisor review to [PROGRESS.md](docs/PROGRESS.md). Commit meaningful increments as you learn.

Your previous work is imported in [completed-work](completed-work/README.md), with source links, cleared notebook outputs, attribution and a record of portability edits. Dataset assets are fetched locally from the originals. Original topic repos remain linked in [GITHUB_EVIDENCE.md](docs/GITHUB_EVIDENCE.md). Do not relabel copied tutorials or generated starters as original implementations. Attribute courses and dataset sources; publish only permitted independent work. Keep restricted graded solutions, private data, credentials and API keys out of Git.

## Foundation completion gate

- [ ] Original linear and logistic regression with loss and optimization explanations.
- [ ] At least three classical ML models compared under a justified evaluation protocol.
- [ ] A PyTorch MLP and CNN with student-written training and validation loops.
- [ ] Error analysis explaining failures and proposed improvements.
- [ ] Every completed module has evidence, reproducible setup, and review.

Choose one specialization after PyTorch. Use the [blueprints](blueprints/README.md) when ready. Scaffold creation does not complete any of these gates.

# My AI foundation portfolio

I am Muhammad Ammar Khalid. I use this repository to record my FYP preparation. I follow my supervisor's **AI Learning and Specialization Guide**, version 1.0 (September 2026).

## Where I am now

I reported on **2026-10-15** that I had completed NumPy, Pandas, Matplotlib, and Seaborn. I had studied scikit-learn through **ColumnTransformer**. My earlier notebooks are in [completed-work](completed-work/README.md). The dates when I studied each topic are unknown.

I still need to check my evidence and add my own explanations. My supervisor has not reviewed these modules yet. I do not mark the full ML or PyTorch foundation complete.

**My next task:** [move from ColumnTransformer to Pipeline](docs/NEXT_STEPS.md). I use [the progress tracker](docs/PROGRESS.md) to record each finished task. [How I add new work](docs/WORKFLOW.md) gives the exact steps.

## Repository map

| Folder | What I put there |
| --- | --- |
| `modules/01-python-data-git` | My Python and data evidence, plus a short diagnostic |
| `modules/02-supervised-ml` | My Course 1 notes and original linear/logistic regression |
| `modules/03-advanced-ml` | My Course 2 work and comparison of at least three models |
| `modules/04-unsupervised-optional` | My optional Course 3 work, if I choose it |
| `modules/05-pytorch-basics` | My PyTorch Basics work |
| `modules/06-pytorch-video-practice` | My independent practice from the beginner videos |
| `modules/07-deep-learning-practice` | My MLP, CNN, training loops, and error analysis |
| `modules/08-evaluation-optional` | My optional evaluation study |
| `practice/sklearn-pipelines` | My next exercise after ColumnTransformer |
| `completed-work` | Copies of my earlier notebooks and source files from 14 repositories |
| `templates` | Forms I use to record experiments, results, and reflections |
| `docs` | My plan, progress, evidence links, and instructions |
| `blueprints` | Plans for my future specialization and capstone repositories |

## Set up Anaconda and Jupyter Notebook

I work from the root of this repository. I use Anaconda, Jupyter Notebook, and uv:

```bash
conda env create -f environment.yml
conda activate fyp-ai
uv pip install -r requirements.txt
python -m ipykernel install --user --name fyp-ai --display-name "FYP AI (Anaconda)"
python scripts/fetch_learning_data.py
python -m notebook
```

I select the **FYP AI (Anaconda)** kernel in Jupyter Notebook. If `fyp-ai` already exists, I activate it. I then start at the `uv pip install` command. The data command is optional for the Pipeline exercise.

**pip option:** I can use `python -m pip install -r requirements.txt` instead of `uv pip install -r requirements.txt`. Both commands use the same package list. [Environment instructions](docs/ENVIRONMENT.md) explain other setup options.

I can run `python practice/sklearn-pipelines/example.py` to see a complete example. Its data is synthetic. The example score is not my FYP result. I then complete [my Pipeline exercise](practice/sklearn-pipelines/exercise.ipynb) myself.

## Record my work

I use [automatic tracking](docs/AUTOMATIC_TRACKING.md) for saved notebooks and changes in my linked GitHub repositories. I can add a short note in [Track_my_learning.ipynb](Track_my_learning.ipynb). The tracker creates a module record and updates [my learning log](docs/LEARNING_LOG.md).

When I finish a task, I save my notebook or code in its module folder. I record the data source, run steps, results, and limits. I write what I learned. I update [PROGRESS.md](docs/PROGRESS.md), then commit and push my changes. [WORKFLOW.md](docs/WORKFLOW.md) shows each step and an example.

My copied notebooks have clear source links and attribution. Their public copies have empty outputs. My original repositories retain their earlier results.

## Foundation completion checks

- [ ] I explain and implement linear and logistic regression myself.
- [ ] I compare at least three classical ML models with a stated evaluation method.
- [ ] I write PyTorch training and validation loops for an MLP and a CNN.
- [ ] I examine model errors and explain possible improvements.
- [ ] I give my supervisor reproducible evidence for each completed module.

I choose one specialization after the PyTorch foundation. I use [the roadmap](docs/ROADMAP.md) and [track plans](blueprints/README.md) when I reach that point.

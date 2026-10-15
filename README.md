# My AI foundation portfolio

I am Muhammad Ammar Khalid. I use this repository to record my FYP preparation. I follow my supervisor's **AI Learning and Specialization Guide**, version 1.0 (September 2026).

## Where I am now

I follow [CampusX: 100 Days of Machine Learning](https://www.youtube.com/playlist?list=PLKnIA16_Rmvbr7zKYQuBfsVkjoLcJgxHH). On **2026-10-15**, I reported **videos 1–31 complete**. Video 31 is Power Transformer. My actual study dates are unknown.

I have also completed NumPy, Pandas, Matplotlib, and Seaborn. My earlier notebooks remain in [completed-work](completed-work/README.md), with their source notes. My playlist index links the relevant notebooks.

**My next lesson:** [video 032 — Binning and Binarization](https://www.youtube.com/watch?v=kKWsJGKcMvo&list=PLKnIA16_Rmvbr7zKYQuBfsVkjoLcJgxHH&index=32).

**[Open my playlist folders and progress](machine-learning/README.md).** I use [my next steps](docs/NEXT_STEPS.md) to continue. I focus on machine learning now. My later guide plans remain available for future use.

**[Tick my completed lesson](https://github.com/AMMARKHALID2004/ai-foundation-portfolio/issues/1).** GitHub Actions updates my lesson index, section counts, and learning records. My video ticks and independent project evidence stay separate. Supervisor review remains pending.

## My active repository map

| Folder | What I put there |
| --- | --- |
| `machine-learning/01-foundations` | Videos 001–014: ML basics and project planning |
| `machine-learning/02-data-and-eda` | Videos 015–022: data sources and EDA |
| `machine-learning/03-feature-engineering` | Videos 023–045: preprocessing, missing data, and outliers |
| `machine-learning/04-dimensionality-reduction` | Videos 046–049: dimensionality and PCA |
| `machine-learning/05-regression` | Videos 050–069: regression, gradients, and regularization |
| `machine-learning/06-logistic-regression` | Videos 070–081: logistic regression and metrics |
| `machine-learning/07-naive-bayes` | Videos 082–090: probability and Naive Bayes |
| `machine-learning/08-neighbors-and-svm` | Videos 091–096: KNN and SVM |
| `machine-learning/09-decision-trees` | Videos 097–100: decision trees |
| `machine-learning/10-ensembles` | Videos 101–127: voting, forests, boosting, and stacking |
| `machine-learning/11-clustering` | Videos 128–132: clustering |
| `machine-learning/12-imbalance-and-tuning` | Videos 133–134: imbalanced data and Optuna |
| `machine-learning/projects` | My original ML implementations and model comparison |
| `completed-work` | My earlier source snapshots and attribution |
| `practice/sklearn-pipelines` | Independent practice for video 029 |
| `docs` and `templates` | My instructions, evidence forms, and supervisor records |

Each lesson section has `notebooks/`, `notes/`, and `results/`. A checked lesson also has a generated record in that section's `learning/` folder. I keep the original `modules/` and `blueprints/` plans for my supervisor's wider guide.

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

I select the **FYP AI (Anaconda)** kernel in Jupyter Notebook. If `fyp-ai` already exists, I activate it. I then start at the `uv pip install` command. I run the data command only when I need the earlier lesson datasets.

**pip option:** I can use `python -m pip install -r requirements.txt` instead of `uv pip install -r requirements.txt`. Both commands use the same package list. [Environment instructions](docs/ENVIRONMENT.md) explain other setup options.

I open [my video 032 exercise](machine-learning/03-feature-engineering/notebooks/video-032-binning-and-binarization.ipynb) in Jupyter Notebook. It is a blank scaffold. I add my own code and observations.

## Record my work

I use [my GitHub checklist](https://github.com/AMMARKHALID2004/ai-foundation-portfolio/issues/1) to record completed topics. GitHub Actions creates a module record and updates [my learning log](docs/LEARNING_LOG.md). I can use this with my computer off. [Tracking instructions](docs/AUTOMATIC_TRACKING.md) explain how I add a new topic.

When I finish a task, I save my notebook or code in its module folder. I record the data source, run steps, results, and limits. I write what I learned and tick the topic. The workflow updates the topic counts in [PROGRESS.md](docs/PROGRESS.md). I record actual study dates and supervisor feedback myself.

My copied notebooks have clear source links and attribution. Their public copies have empty outputs. My original repositories retain their earlier results.

## My ML evidence checks

- [ ] I explain and implement linear and logistic regression myself.
- [ ] I compare at least three classical ML models with a stated evaluation method.
- [ ] I examine model errors and explain possible improvements.
- [ ] I give my supervisor reproducible evidence for my ML work.

I keep the original wider foundation requirements in [the guide map](docs/GUIDE_MAPPING.md). Watching this playlist does not confirm those requirements or supervisor approval.

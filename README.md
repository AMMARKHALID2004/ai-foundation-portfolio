# My data libraries and machine learning portfolio

I am Muhammad Ammar Khalid. I use this repository for NumPy, Pandas, Matplotlib, Seaborn, and machine learning.

I have completed the four data libraries. My ML learning currently covers foundations, data work, and preprocessing through power transformations. My actual study dates are unknown. I keep my learning claims, independent exercises, and supervisor review separate.

## My folders

| Folder | My work |
| --- | --- |
| [numpy](numpy/README.md) | Arrays, indexing, broadcasting, operations, and reference exercises |
| [pandas](pandas/README.md) | Series, DataFrames, grouping, joins, strings, and dates |
| [matplotlib](matplotlib/README.md) | Plotting and figure practice |
| [seaborn](seaborn/README.md) | Statistical plots and visual analysis |
| [machine-learning](machine-learning/README.md) | Data collection, cleaning, EDA, preprocessing, models, evaluation, and projects |

Each topic has space for my notebooks, notes, and results. My earlier GitHub work is stored in these folders. [My source records](docs/IMPORTED_WORK.md) identify each repository and commit.

**My next topic:** [binning and binarization](machine-learning/preprocessing/notebooks/binning-and-binarization.ipynb). I use this blank notebook for my own practice.

**[Update my learning checklist](https://github.com/AMMARKHALID2004/ai-foundation-portfolio/issues/1).** GitHub Actions updates [my progress](docs/PROGRESS.md) and creates a record in the matching topic folder. [Tracking instructions](docs/AUTOMATIC_TRACKING.md) explain the steps.

## My Anaconda and Jupyter setup

I work from this repository's root. I create the study environment once:

```bash
conda env create -f environment.yml
conda activate fyp-ai
uv pip install -r requirements.txt
python -m ipykernel install --user --name fyp-ai --display-name "FYP AI (Anaconda)"
python -m notebook
```

If `fyp-ai` already exists, I activate it and continue with the package command. I select the **FYP AI (Anaconda)** kernel in Jupyter Notebook. I keep my existing environments.

**pip alternative:** I use `python -m pip install -r requirements.txt` in place of the uv command. [My environment guide](docs/ENVIRONMENT.md) has the full instructions.

I can fetch the earlier lesson assets locally with `python scripts/fetch_learning_data.py`. They remain ignored by Git. The cricket project has its own dependencies and data requirements; I read its source notes before I run it.

## How I continue

1. I open the matching library or ML topic folder.
2. I save my own notebook, notes, sources, and results there.
3. I run my work from a fresh Jupyter kernel.
4. I commit and push the files. I tick the completed topic in my GitHub issue.
5. I wait for Actions, then commit any local edits and run `git pull --ff-only` to get its updates.

I read [my workflow](docs/WORKFLOW.md) and [my next steps](docs/NEXT_STEPS.md) when I need more detail. Imported notebooks keep their source attribution. Their copied outputs are cleared; the original repositories retain historical results.

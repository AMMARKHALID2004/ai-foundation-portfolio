# Your existing foundation work

Imported from **14 existing GitHub repositories** on 2026-10-15: **55 notebooks within 134 notebook/source files**, plus source notes and this index. Another 56 supporting asset files are available through the original repos and the download command below. Historical results remain available in the linked original repositories; copied notebooks start with cleared outputs. The library-study completion reported by the student is credited in [the progress tracker](../docs/PROGRESS.md); imports alone do not establish supervisor approval or complete the remaining ML/PyTorch pathway.

| Work | Notebooks | Published notebook/source files | Source |
| --- | --- | --- | --- |
| [Python_OOP](python/oop/SOURCE.md) | 1 | 30 | [Original repo](https://github.com/AMMARKHALID2004/Python_OOP) |
| [Python-Revision](python/revision/SOURCE.md) | 1 | 1 | [Original repo](https://github.com/AMMARKHALID2004/Python-Revision) |
| [Advance-Python](python/advanced/SOURCE.md) | 7 | 21 | [Original repo](https://github.com/AMMARKHALID2004/Advance-Python) |
| [generators-and-decorators](python/generators-decorators/SOURCE.md) | 0 | 14 | [Original repo](https://github.com/AMMARKHALID2004/generators-and-decorators) |
| [Numpy](numpy/SOURCE.md) | 14 | 16 | [Original repo](https://github.com/AMMARKHALID2004/Numpy) |
| [Numpy-100-Problems](numpy-exercises/SOURCE.md) | 2 | 13 | [Original repo](https://github.com/AMMARKHALID2004/Numpy-100-Problems) |
| [Pandas](pandas/SOURCE.md) | 10 | 12 | [Original repo](https://github.com/AMMARKHALID2004/Pandas) |
| [Matplotlib](matplotlib/SOURCE.md) | 2 | 4 | [Original repo](https://github.com/AMMARKHALID2004/Matplotlib) |
| [Seaborn](seaborn/SOURCE.md) | 2 | 4 | [Original repo](https://github.com/AMMARKHALID2004/Seaborn) |
| [Working-with-different-files](data-loading/SOURCE.md) | 4 | 4 | [Original repo](https://github.com/AMMARKHALID2004/Working-with-different-files) |
| [Data-Cleaning](data-cleaning/SOURCE.md) | 2 | 3 | [Original repo](https://github.com/AMMARKHALID2004/Data-Cleaning) |
| [EDA](eda/SOURCE.md) | 1 | 1 | [Original repo](https://github.com/AMMARKHALID2004/EDA) |
| [EDA-Project](eda-project/SOURCE.md) | 3 | 3 | [Original repo](https://github.com/AMMARKHALID2004/EDA-Project) |
| [Machine-Learning](sklearn-preprocessing/SOURCE.md) | 6 | 8 | [Original repo](https://github.com/AMMARKHALID2004/Machine-Learning) |

## Start with your completed library material

- [NumPy arrays/indexing/broadcasting](numpy/SOURCE.md).
- [Pandas, joins, GroupBy, strings and dates](pandas/SOURCE.md).
- [Matplotlib](matplotlib/SOURCE.md) and [Seaborn](seaborn/SOURCE.md).
- [scikit-learn preprocessing through ColumnTransformer](sklearn-preprocessing/SOURCE.md).

Python practice, data loading/cleaning and EDA are also kept here. The NumPy-100 collection retains its upstream MIT licence and attribution; supplied solutions are reference material, not a claim of independent completion.

Use the [Anaconda + uv + Jupyter Notebook setup](../docs/ENVIRONMENT.md). Open each notebook from its folder; run scripts from the relevant lesson folder when they use local imports. [Import notes](../docs/IMPORTED_WORK.md) identify missing external datasets, optional tools, API/local-database lessons and deliberate error demonstrations. [The manifest](../docs/import-manifest.json) records source commits, per-file hashes and modifications.

## Get the lesson datasets locally

After GitHub CLI is installed (and signed in where needed):

```bash
python scripts/fetch_learning_data.py
# Or just one topic:
python scripts/fetch_learning_data.py --repo Pandas
```

The downloader uses each original repository's recorded commit and verifies file hashes. Assets are placed beside their lesson notebooks and ignored by Git; it does not upload them. Existing different local files are preserved. `--list` previews the files. The original datasets and their source permissions remain with the original repos.

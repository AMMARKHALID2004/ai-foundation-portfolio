# My earlier foundation work

I brought work from **14 of my GitHub repositories** into this portfolio on 2026-10-15. It includes **55 notebooks within 134 notebook/source files**. Another 56 supporting files are available from the original repositories. My original saved results remain there. The public notebook copies have empty outputs. I record my reported library progress in [the tracker](../docs/PROGRESS.md). My supervisor has not reviewed these modules yet.

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

## Review the libraries I studied

- [NumPy arrays/indexing/broadcasting](numpy/SOURCE.md).
- [Pandas, joins, GroupBy, strings and dates](pandas/SOURCE.md).
- [Matplotlib](matplotlib/SOURCE.md) and [Seaborn](seaborn/SOURCE.md).
- [scikit-learn preprocessing through ColumnTransformer](sklearn-preprocessing/SOURCE.md).

Python practice, data loading/cleaning and EDA are also kept here. The NumPy-100 collection retains its upstream MIT licence and attribution; supplied solutions are reference material, not a claim of independent completion.

I use [my Anaconda, uv, and Jupyter Notebook setup](../docs/ENVIRONMENT.md). I open each notebook from its folder. I run scripts from their lesson folder when they use local imports. [The import notes](../docs/IMPORTED_WORK.md) list missing data, optional tools, API and database lessons, and intentional error examples. [The manifest](../docs/import-manifest.json) records source commits and file hashes.

## Get the lesson datasets locally

After I sign in to GitHub CLI, I run:

```bash
python scripts/fetch_learning_data.py
# Or just one topic:
python scripts/fetch_learning_data.py --repo Pandas
```

The script reads each source file at its recorded commit and checks its hash. It puts the file beside its lesson notebook. Git ignores the file. The script keeps an existing local file if its content differs. I use `--list` to see the files before I download them.

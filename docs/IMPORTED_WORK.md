# My imported work

I brought my existing library and ML work into the matching topic folders. I checked the source repositories on 2026-10-15. My source snapshots keep their attribution and licence. Their copied notebook outputs are empty. Original repositories retain earlier results.

| Source repository | My folder | Notebooks | Source commit |
| --- | --- | --- | --- |
| [Numpy](https://github.com/AMMARKHALID2004/Numpy) | [numpy/notebooks](../numpy/notebooks/SOURCE.md) | 14 | `e05b96d2b509` |
| [Numpy-100-Problems](https://github.com/AMMARKHALID2004/Numpy-100-Problems) | [numpy/exercises/reference](../numpy/exercises/reference/SOURCE.md) | 2 | `6429dce2bcb9` |
| [Pandas](https://github.com/AMMARKHALID2004/Pandas) | [pandas/notebooks](../pandas/notebooks/SOURCE.md) | 10 | `26f59fd03a67` |
| [Matplotlib](https://github.com/AMMARKHALID2004/Matplotlib) | [matplotlib/notebooks](../matplotlib/notebooks/SOURCE.md) | 2 | `be79ccd914c9` |
| [Seaborn](https://github.com/AMMARKHALID2004/Seaborn) | [seaborn/notebooks](../seaborn/notebooks/SOURCE.md) | 2 | `7af9f648b944` |
| [Working-with-different-files](https://github.com/AMMARKHALID2004/Working-with-different-files) | [machine-learning/data-collection/notebooks](../machine-learning/data-collection/notebooks/SOURCE.md) | 4 | `ce980db84675` |
| [Data-Cleaning](https://github.com/AMMARKHALID2004/Data-Cleaning) | [machine-learning/data-cleaning/notebooks](../machine-learning/data-cleaning/notebooks/SOURCE.md) | 2 | `1147bbabad00` |
| [EDA](https://github.com/AMMARKHALID2004/EDA) | [machine-learning/exploratory-data-analysis/notebooks/reference](../machine-learning/exploratory-data-analysis/notebooks/reference/SOURCE.md) | 1 | `1918023702a8` |
| [EDA-Project](https://github.com/AMMARKHALID2004/EDA-Project) | [machine-learning/exploratory-data-analysis/notebooks/projects](../machine-learning/exploratory-data-analysis/notebooks/projects/SOURCE.md) | 3 | `d6571bf8f910` |
| [Machine-Learning](https://github.com/AMMARKHALID2004/Machine-Learning) | [machine-learning/preprocessing/notebooks](../machine-learning/preprocessing/notebooks/SOURCE.md) | 6 | `fdc57ebf9531` |
| [Cricket-Match-Win-Probability-Predictor](https://github.com/AMMARKHALID2004/Cricket-Match-Win-Probability-Predictor) | [machine-learning/projects/cricket-win-probability](../machine-learning/projects/cricket-win-probability/SOURCE.md) | 1 | `d846ec32c6a7` |

## My source records

[The manifest](import-manifest.json) records each source commit, source hash, imported hash, local folder, and any portability or output-clearing edits. I do not claim that source code, reference solutions, or tutorial reproductions are independent work.

I moved the existing snapshots with their internal folders intact. Data paths remain relative to each source folder. I open an imported notebook from its own folder when it uses relative paths.

## My supporting data

My earlier lesson assets remain ignored locally. I use `python scripts/fetch_learning_data.py --list` to inspect their recorded paths. I use `python scripts/fetch_learning_data.py --repo Pandas` to fetch one repository’s assets. The helper checks hashes and preserves a different existing local file.

Some data and cleaning lessons need external APIs, a local database, or restricted example data. Some cells intentionally show errors. I inspect the source notes before I run them. The cricket project has separate dependencies and excluded datasets/models; I read its SOURCE.md.

I keep original source notes intact. A historical import date in those notes describes the earlier copy. The current manifest records this structure and the latest checked commits.

# Existing GitHub evidence

Account: [AMMARKHALID2004](https://github.com/AMMARKHALID2004). Inventory inspected on **2026-10-15**. The ColumnTransformer notebook source was read; other entries are based on repository file inventories. This is not a full execution, originality review, or supervisor sign-off.

| Area | Existing repository | Observed work | Next evidence task |
| --- | --- | --- | --- |
| NumPy | [Numpy](https://github.com/AMMARKHALID2004/Numpy) | Arrays, operations, indexing, broadcasting, missing values and array transformations | Select an independently explained extension and document setup/results |
| NumPy exercises | [Numpy-100-Problems](https://github.com/AMMARKHALID2004/Numpy-100-Problems) | Exercise and supplied solution materials, licence and generators | Distinguish upstream exercises/solutions from personal original work; retain attribution |
| Pandas | [Pandas](https://github.com/AMMARKHALID2004/Pandas) | Series, DataFrames, GroupBy, joins, MultiIndex, strings and dates | Run representative notebooks, record dataset sources and original extensions |
| Matplotlib | [Matplotlib](https://github.com/AMMARKHALID2004/Matplotlib) | Two plotting notebooks and datasets | Publish selected labelled figures and interpretations |
| Seaborn | [Seaborn](https://github.com/AMMARKHALID2004/Seaborn) | Two session notebooks | Document data sources and independent chart interpretation |
| Data handling | [Data-Cleaning](https://github.com/AMMARKHALID2004/Data-Cleaning) | Wrangling/cleaning notebooks and CSV/XLSX assets | Confirm provenance and permissions; explain cleaning decisions |
| EDA project | [EDA-Project](https://github.com/AMMARKHALID2004/EDA-Project) | Cleaning, EDA and bivariate notebooks | State problem, data source, findings and limitations |
| scikit-learn | [Machine-Learning](https://github.com/AMMARKHALID2004/Machine-Learning) | Scaling, encoding, power transformation and ColumnTransformer | Correct portability and manual feature order; add Pipeline practice next |

These links acknowledge prior learning without moving notebooks or making their completion dates up. The complete refresh module also requires Python/OOP, environments, command-line and Git skills; those are not established by these file inventories alone.

## ColumnTransformer review notes

File: [Column Transformer.ipynb](https://github.com/AMMARKHALID2004/Machine-Learning/blob/master/Column%20Transformer/Column%20Transformer.ipynb).

- Dataset loading uses an absolute local path. A repo-relative dataset location is needed for reproduction.
- Manual training features are concatenated as **age, cough, gender/city, fever**, while manual test features are **age, fever, gender/city, cough**. Equal array shapes conceal this semantic mismatch.
- The split has no fixed random seed. The target-training variable is named `t_train`; `y_train` would make intent clearer.
- One-hot encoding does not define how unseen categories should be handled.
- A displayed shape expression repeats the test array instead of showing train and test.
- The ColumnTransformer section correctly fits on training data and transforms test data. A Pipeline is the next extension for adding a model and cross-validation.

## Review and publishing status

The separate [ai-foundation-portfolio repository](https://github.com/AMMARKHALID2004/ai-foundation-portfolio) follows the supervisor's preferred foundation structure. Existing topic notebooks remain in their original repositories and are linked here.

Use [GITHUB_CHANGES.md](GITHUB_CHANGES.md) for actual publication and draft pull request status. A draft pull request does not change the default branch; integration requires merging it. The supplied setup is not completed coursework or supervisor approval.

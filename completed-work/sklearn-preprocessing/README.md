# Machine Learning learning portfolio

scikit-learn preprocessing notebooks and FYP common-foundation preparation, following the supervisor's AI Learning and Specialization Guide, version 1.0 (September 2026).

## Current position

As reported on 2026-10-15, study has reached **ColumnTransformer**. This establishes a preprocessing learning checkpoint; ML Course 1/2, from-scratch regression, PyTorch and the complete common foundation are not yet confirmed.

## Existing notebooks

| Topic | Notebook |
| --- | --- |
| Standardization | [Z-score scaling](Standardization%20%28Z-score%20Normalization%29/Standardization.ipynb) |
| Normalization | [Normalization](Normalization/Normalization.ipynb) |
| Ordinal / label encoding | [Ordinal and Label Encoding](Ordinal%20Encoding/Ordinal%20and%20Label%20Encoding.ipynb) |
| One-hot encoding | [One hot encoder](One%20hot%20encoder/One%20hot%20encoder.ipynb) |
| ColumnTransformer | [Column Transformer](Column%20Transformer/Column%20Transformer.ipynb) |
| Power transformations | [Power Transformer](Power%20Transformer/Power%20Transformer.ipynb) |

## Supervisor-aligned foundation

The separate [foundation portfolio](https://github.com/AMMARKHALID2004/ai-foundation-portfolio) contains the roadmap, tracker, prior-evidence links, eight ordered common-foundation modules, evidence templates and future track/capstone plans. The foundation follows the supervisor's preferred separate-repository structure; the capstone should also use a separate repo.

**Continue here:** [next tasks](https://github.com/AMMARKHALID2004/ai-foundation-portfolio/blob/main/docs/NEXT_STEPS.md). Credit the completed NumPy/Pandas/Matplotlib/Seaborn work; connect ColumnTransformer to a model Pipeline, then complete the required ML concepts and PyTorch before choosing one specialization.

## Reproduce the ColumnTransformer notebook

Use Python 3.11+, create/activate a virtual environment and install `requirements.txt`. Open Jupyter from the repository root or the `Column Transformer` folder and run all cells in the notebook. Its included `covid_toy.csv` is a teaching dataset; document its upstream source/licence before treating it as project data. The notebook's dataset path is relative, split fixed/stratified, and manual training/test feature orders aligned. Other older notebooks may still contain machine-specific paths and need individual review.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m jupyter lab
```

For the synthetic Pipeline example, use the separate foundation repository's setup instructions and run `python practice/sklearn-pipelines/example.py` there.

## Evidence still to add

Actual study/completion dates, independent extensions, dataset/tutorial attribution, environment versions, results and interpretations, reflections, and supervisor initials/review dates. Scaffolded examples and documentation are assistance, not completed student implementations. Do not upload restricted graded solutions, private datasets or credentials. `.gitignore` prevents new checkpoint files; already tracked checkpoints are retained in this change.

# Your next tasks

## 1. Package what you already know

Your existing notebooks are now imported in [completed-work](../completed-work/README.md). Use them as evidence; do not repeat full beginner courses. Pick representative notebooks, restart the kernel and run all cells, replace absolute dataset paths, add setup and dataset provenance, and write one short independent extension and reflection. Record actual learning dates if known; otherwise leave them unknown.

The reviewed ColumnTransformer notebook shows prior train/test splitting, imputation, one-hot and ordinal encoding. Its previous manual train and test arrays used different feature orders; that correction is now merged. Keep the same order and explain why equal shapes do not guarantee equivalent features. The merged notebook already uses a relative dataset path, `random_state`, and an unseen-category policy. A supplied correction is assistance; explain and reproduce it yourself.

## 2. Bridge from ColumnTransformer to Pipeline

1. Run `python practice/sklearn-pipelines/example.py` from the repo root.
2. Read the code: data split → preprocessing fitted inside a Pipeline → model → evaluation.
3. Complete `practice/sklearn-pipelines/exercise.ipynb` independently.
4. Explain why fitting imputation/scaling before splitting or before cross-validation leaks information.
5. Add your metrics, one figure, a limitation, an original extension, and reflection; commit them.

References: [Pipelines and ColumnTransformer](https://scikit-learn.org/stable/modules/compose.html), [common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html).

## 3. Complete the required ML foundation

Start or verify Course 1 concepts: linear/logistic regression, loss, gradient descent, scaling and regularization. Preprocessing competence alone does not establish these. Publish original independent implementations, not graded assignment answers. Then cover Course 2, compare at least three models, and proceed to PyTorch.

Optional Course 3 can be skipped or deferred without blocking the required foundation. Optional evaluation study is useful, while sound evaluation still belongs in every required project.

## 4. First supervision checkpoint

Bring the evidence index, your independent Pipeline exercise, initial Course 1 implementation, and the updated progress tracker. Ask the supervisor to review the evidence and record review dates. Choose a track after the PyTorch foundation, as the guide requires.

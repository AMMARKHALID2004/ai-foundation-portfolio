# ColumnTransformer to Pipeline practice

This is a supplied teaching starter, not evidence that the student has completed ML Course 1 or an original model-comparison project.

Run from the foundation repository root:

```bash
python practice/sklearn-pipelines/example.py
```

The example generates a small synthetic mixed-type classification dataset, splits it before fitting preprocessing, and fits a `ColumnTransformer` and logistic regression together in a `Pipeline`. Five-fold stratified cross-validation uses only the training partition; the separate test partition is evaluated after fitting. The printed metrics demonstrate the mechanics on synthetic data, not real-world performance.

Use [exercise.ipynb](exercise.ipynb) to implement an original extension independently. Start with a dummy baseline and compare at least three meaningful models once you understand their assumptions. Declare your metric and selection procedure before final testing. For repeated model development, use validation/cross-validation rather than repeatedly consulting the test set.

Completion evidence: your own code, configurations, validation scores and spread, one justified figure, held-out result after selection, an error-analysis note and learning reflection. Link these in the progress tracker. The completed three-model comparison can then contribute to Module 3 after review.

Data source: locally generated synthetic data; no external dataset, API or medical use. Seed: 42. Python and dependency versions should be recorded with your experiment.

References: [scikit-learn composition](https://scikit-learn.org/stable/modules/compose.html) and [leakage pitfalls](https://scikit-learn.org/stable/common_pitfalls.html).

# Preparation verification

Checked **2026-10-15**, in a temporary Python **3.12.14** environment with NumPy **2.5.4**, Pandas **3.0.6**, and scikit-learn **1.9.1**.

## Passed

- Foundation Markdown links point to existing local files.
- Python files and both notebook code sources parse; notebook schemas validate.
- Synthetic Pipeline example runs end to end with fixed seed 42, a 180/60 split, training-only five-fold cross-validation and a held-out evaluation.
- The Pipeline handles an unseen categorical value and produces finite probabilities.
- Fitted imputation statistics match the training partition alone.
- Corrected ColumnTransformer notebook code cells run from both the notebook folder and repository root using its existing toy CSV.
- Manual training/test feature order matches; ColumnTransformer outputs have matching widths and finite values.

Example smoke-run metrics: CV F1 mean **0.8964**, standard deviation **0.0503**, held-out F1 **0.8525**. These are supplied-example results on artificial data, not the student's experiments or FYP performance. Do not use them to mark a module complete.

The exact core example dependency set is in `requirements-example-lock.txt`. The broader plotting/JupyterLab environment in `requirements.txt` and other historical notebooks have not all been validated. PyTorch/track/capstone work has not been implemented or claimed complete.

## GitHub limits

Account and repository reads succeeded. Creating a review branch and tree was denied with GitHub **403: Resource not accessible by integration**; no successful remote writes or pull requests exist yet. The GitHub plugin is installed, but its installation listing was empty. The terminal login token was invalid, and the in-app browser requires sign-in. Prepared uploads remain local until usable write access is established.

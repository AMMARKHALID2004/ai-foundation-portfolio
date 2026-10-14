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

## GitHub publication

Initial connector writes were denied and the terminal login was expired. The existing GitHub CLI authorization was subsequently refreshed, and the separate foundation repo was created through the signed-in browser. Final publication and pull request links are recorded in [GITHUB_CHANGES.md](GITHUB_CHANGES.md).

Five existing-repository patches were checked against their observed baselines. Other historical notebooks have not all been executed; their README additions state this limit explicitly.

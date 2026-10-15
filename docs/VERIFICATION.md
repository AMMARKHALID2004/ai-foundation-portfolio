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

Example smoke-run metrics: CV F1 mean **0.8964**, standard deviation **0.0503**, held-out F1 **0.8525**. These are supplied-example results on artificial data. They are not my experiments or FYP performance. I do not use them to mark a module complete.

The exact core example dependency set is in `requirements-example-lock.txt`. The broader plotting/JupyterLab environment in `requirements.txt` and other historical notebooks have not all been validated. PyTorch/track/capstone work has not been implemented or claimed complete.

## GitHub publication

Initial connector writes were denied and the terminal login was expired. The existing GitHub CLI authorization was subsequently refreshed, and the separate foundation repo was created through the signed-in browser. Final publication and pull request links are recorded in [GITHUB_CHANGES.md](GITHUB_CHANGES.md).

Five existing-repository patches were checked against their observed baselines. Other historical notebooks have not all been executed; their README additions state this limit explicitly.

## Consolidation checks — 2026-10-15

- All five original pull requests were merged and GitHub confirmed their merge commits.
- 134 public notebook/source hashes and 56 local-only asset hashes match the manifest; unchanged source files match their original hashes.
- All 55 imported notebook schemas validate; new documentation links and `environment.yml` validate.
- Representative imported NumPy, Pandas, and corrected ColumnTransformer notebooks executed without errors in my installed Anaconda environment.
- The Pipeline starter also ran on Anaconda Python 3.14.6, NumPy 2.5.3, Pandas 3.0.6 and scikit-learn 1.9.0, with the same previously recorded synthetic-example scores.
- Original saved outputs remain in their source repositories. Public notebook copies have empty outputs. Verification runs did not replace my original results. My base environment was not changed.

The fresh conda environment YAML and uv/pip instructions are documented; a new conda environment was not installed for this documentation/import task. Full execution of every archived lesson is not claimed. Optional profiling/OpenCV packages, missing external datasets and API/database services are identified in [import notes](IMPORTED_WORK.md).

The final public payload contains notebook/source files only, with outputs and embedded widget/attachment data cleared. Supporting assets are excluded from public history and ignored locally; the GitHub CLI downloader retrieves them from recorded original commits.

The dataset helper passed a real GitHub CLI download and hash check using a small existing cricket CSV. It also preserved a different local file and rejected an asset path outside the project.

## Learning tracker checks — 2026-10-15

- Seven tests cover baseline scans, new and changed files, repeat scans, preserved notes, GitHub failures, module assignment, and date/path checks.
- The initial GitHub scan succeeded for all 14 configured repositories. It recorded no new learning claims.
- A second local scan made no file changes.
- The tracker uses the Python standard library. It does not execute notebook code.
- The initial Codex hourly schedule was later disabled at my request. The replacement is a GitHub issue checklist and GitHub Actions.

## GitHub checklist checks — 2026-10-15

- Thirteen tests pass, including ticking, unticking, repeat runs, new topics, removed topics, and preserved reflection notes and supervisor reviews.
- The checklist starts with only my five previously reported completed topics checked.
- Check counts update automatically. Study dates and supervisor approval are not inferred.

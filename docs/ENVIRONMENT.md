# Anaconda, uv and Jupyter Notebook

The student's preferred workflow is **Anaconda + Jupyter Notebook**, with **uv** for package installation. pip is supported for anyone using it instead. GitHub work uses `gh` and Git.

## Anaconda with uv — primary workflow

From the repository root in Anaconda Prompt or a conda-enabled terminal:

```bash
conda env create -f environment.yml
conda activate fyp-ai
uv pip install -r requirements.txt
python -m ipykernel install --user --name fyp-ai --display-name "FYP AI (Anaconda)"
python scripts/fetch_learning_data.py
python -m notebook
```

`environment.yml` creates the dedicated Python 3.12 environment and installs uv/pip from conda-forge. The activated conda environment is detected by uv. In Jupyter Notebook, select **FYP AI (Anaconda)** as the kernel. A server started from Anaconda's base environment can also use that registered kernel.

If `fyp-ai` already exists, activate it and continue from dependency installation instead of recreating it. If you already have a suitable study environment, you can activate that environment and register a separate kernel name; changing base is unnecessary.

## pip alternative

Use the same conda environment and replace the uv installation step with:

```bash
python -m pip install -r requirements.txt
```

Then register the kernel and launch Jupyter Notebook as above. Either installer uses the same dependency file.

## uv without Anaconda

```bash
uv venv --python 3.12
uv pip install --python .venv -r requirements.txt
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m notebook
```

Select the virtual environment's Python kernel, or activate `.venv` and register it with a distinct name. On macOS/Linux, activation is `source .venv/bin/activate`; in Windows PowerShell it is `.venv\Scripts\Activate.ps1`.

## pip without Anaconda

```bash
python -m venv .venv
```

Activate `.venv` for your platform, then:

```bash
python -m pip install -r requirements.txt
python -m notebook
```

## Optional historical lessons

Selected EDA lessons import ydata-profiling, PyGWalker and AutoViz; one generator demo imports OpenCV. They are separated from the core environment:

```bash
conda activate fyp-ai
uv pip install -r requirements-optional.txt
# pip alternative:
python -m pip install -r requirements-optional.txt
```

Those optional libraries and external API/database lessons are not required to reproduce the offline Pipeline starter. Some archived notebooks deliberately demonstrate errors or need datasets/local services not present in the source repositories; consult [import notes](IMPORTED_WORK.md).

## Run and record your work

```bash
python practice/sklearn-pipelines/example.py
uv pip freeze > requirements-lock.txt
# pip alternative:
python -m pip freeze > requirements-lock.txt
```

Record Python/package versions with each experiment. Open notebooks from their stored folders so their relative data paths work. The public snapshots have cleared outputs; original historical results stay in the source repos. Retrieve supporting data with `python scripts/fetch_learning_data.py` and rerun individual lessons when reviewing your own evidence.

The local Anaconda installation was checked on 2026-10-15: Python 3.14.6, NumPy 2.5.3, Pandas 3.0.6, scikit-learn 1.9.0, Matplotlib 3.11.0, Seaborn 0.13.2 and Notebook 7.5.7. The documented fresh environment targets Python 3.12 for the broader optional library ecosystem; the student's base environment was not changed.

References: [uv environment discovery](https://docs.astral.sh/uv/pip/environments/), [conda environments](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html), [IPython kernel registration](https://ipython.readthedocs.io/en/stable/install/kernel_install.html).

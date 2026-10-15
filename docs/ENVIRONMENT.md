# My Anaconda and Jupyter Notebook setup

I use Anaconda and Jupyter Notebook. I prefer uv to install Python packages. I keep pip commands for people who use pip. I use GitHub CLI and Git for repository work.

## My Anaconda setup

I run these commands from the repository root in a terminal with conda enabled:

```bash
conda env create -f environment.yml
conda activate fyp-ai
uv pip install -r requirements.txt
python -m ipykernel install --user --name fyp-ai --display-name "FYP AI (Anaconda)"
python -m notebook
```

The `environment.yml` file creates a Python 3.12 environment. I select **FYP AI (Anaconda)** in Jupyter Notebook. If `fyp-ai` already exists, I activate it and start with the `uv pip install` command. I can also register a different study environment with its own kernel name.

I get data for earlier lessons with `python scripts/fetch_learning_data.py`. I can skip this command for the Pipeline starter. The script retrieves files from the original repositories and checks their hashes. It does not add them to Git.

## pip option

I can replace the uv installation command with:

```bash
python -m pip install -r requirements.txt
```

I then register the kernel and start Jupyter Notebook as shown above. Both installers use `requirements.txt`.

## uv without Anaconda

```bash
uv venv --python 3.12
uv pip install --python .venv -r requirements.txt
source .venv/bin/activate
python -m notebook
```

On Windows PowerShell, I activate the environment with `.venv\Scripts\Activate.ps1`. I select this environment's Python kernel in Jupyter Notebook.

## pip without Anaconda

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m notebook
```

On Windows PowerShell, I use `.venv\Scripts\Activate.ps1` to activate the environment.

## Optional packages and earlier lessons

Some earlier EDA lessons use ydata-profiling, PyGWalker, or AutoViz. One generator example uses OpenCV. I install these packages only when I need them:

```bash
conda activate fyp-ai
uv pip install -r requirements-optional.txt
```

I can use `python -m pip install -r requirements-optional.txt` instead. Some earlier lessons need an external API or a local database. Other lessons show errors on purpose. I read [the import notes](IMPORTED_WORK.md) before I run them.

## Record my environment

I record Python and package versions with each experiment. I open each notebook from its folder when it uses relative data paths. I restart the kernel and run all required cells before I report a result. I can run `python practice/sklearn-pipelines/example.py` from the repository root to check the core setup.

On 2026-10-15, my installed Anaconda base had Python 3.14.6, NumPy 2.5.3, Pandas 3.0.6, scikit-learn 1.9.0, Matplotlib 3.11.0, Seaborn 0.13.2, and Notebook 7.5.7. The `environment.yml` file requests Python 3.12 for a new `fyp-ai` environment.

References: [uv environment discovery](https://docs.astral.sh/uv/pip/environments/), [conda environments](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html), and [IPython kernel registration](https://ipython.readthedocs.io/en/stable/install/kernel_install.html).

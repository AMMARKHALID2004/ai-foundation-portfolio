# 🏏 Cricket Match Win Probability Predictor

A machine learning web app that predicts **pre-match win probabilities** for T20 cricket matches. Pick two teams, a venue, and toss details — the app pulls each team's recent form and head-to-head history automatically, then an XGBoost model trained on historical match data returns a calibrated win probability for each side.

Built with a **FastAPI** backend serving the ML model and a **Streamlit** frontend for the interactive dashboard.

---

## Features

- **Pre-match win prediction** — win probability for both teams based on team strength (Elo ratings), recent form, head-to-head record, venue, and toss outcome
- **Team analytics** — historical win rate, batting-first vs. bowling-first win rate per team
- **Head-to-head dashboard** — total wins between two teams plus their last 5 meetings
- **Elo rating history** — see how a team's strength rating has evolved over time
- **Interactive UI** — built with Streamlit, with Plotly charts for visualizing probabilities

---

## Tech Stack

| Layer | Tools |
|---|---|
| Backend / API | FastAPI, Uvicorn |
| Modeling | XGBoost, scikit-learn, pandas, NumPy |
| Frontend | Streamlit, Plotly |
| Model storage | Joblib |
| Packaging | [uv](https://docs.astral.sh/uv/) |

---

## Project Structure

```text
Cricket-Match-Win-Probability-Predictor/
├── backend/
│   └── main.py                  # FastAPI app: prediction, stats, analytics endpoints
├── frontend/
│   └── app.py                   # Streamlit dashboard (calls the FastAPI backend)
├── data/
│   ├── matchwise_data.csv       # Raw match-level data
│   ├── cleaned_base_data.csv    # Cleaned data used by the backend at runtime
│   ├── pre_match_features.csv   # Engineered features used for training
│   ├── data_prep.py             # Cleans raw data
│   └── feature_engineering.py   # Builds model features (Elo, form, H2H, venue stats)
├── models/
│   ├── train_model.py           # Trains and saves the XGBoost model
│   └── saved_models/            # Trained model + column schema (.joblib)
├── t20s_json/                   # Raw ball-by-ball T20 match data (source dataset)
├── pyproject.toml               # Project dependencies (used by uv)
├── uv.lock                      # Locked dependency versions
├── requirements.txt             # Same dependencies, for pip users
└── Dockerfile                   # Container build for deployment
```

---

## Getting Started

### 1. Install `uv`

This project uses [uv](https://docs.astral.sh/uv/) — a fast Python package manager — instead of plain `pip` + `venv`. If you don't have it installed yet, pick your platform below:

**macOS / Linux** (terminal):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows** (PowerShell):
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Alternative (any OS, if you already have Python + pip):**
```bash
pip install uv
```

**Or with a package manager:**
```bash
# macOS (Homebrew)
brew install uv

# Windows (winget)
winget install --id=astral-sh.uv -e

# Windows (Scoop)
scoop install uv
```

After installing, restart your terminal and verify it worked:
```bash
uv --version
```

> 💡 uv automatically installs and manages the correct Python version for this project too — you don't need Python pre-installed. If you'd rather use your own Python + pip, see the [pip alternative](#alternative-using-pip-without-uv) below.

### 2. Clone the repository

```bash
git clone https://github.com/AMMARKHALID2004/Cricket-Match-Win-Probability-Predictor.git
cd Cricket-Match-Win-Probability-Predictor
```

### 3. Install dependencies

```bash
uv sync
```

This creates a `.venv` folder and installs every dependency pinned in `uv.lock` — no manual virtual environment setup needed.

### 4. Run the app

The app has two parts that need to run at the same time: the **FastAPI backend** (serves predictions) and the **Streamlit frontend** (the dashboard you interact with).

**Terminal 1 — start the backend:**
```bash
uv run uvicorn backend.main:app --reload --port 8000
```

**Terminal 2 — start the frontend:**
```bash
uv run streamlit run frontend/app.py
```

Then open your browser at:
```
http://localhost:8501
```

The Streamlit app talks to the backend at `http://127.0.0.1:8000` by default. If you run the backend on a different host/port, set the `API_URL` environment variable before launching Streamlit, e.g.:

```bash
export API_URL="http://127.0.0.1:8000"   # macOS/Linux
set API_URL=http://127.0.0.1:8000        # Windows (cmd)
```

---

## (Re)training the model

The repo ships with a pre-trained model in `models/saved_models/`, so you don't need to retrain anything to run the app. If you want to reproduce or update it:

```bash
uv run python data/data_prep.py          # clean raw match data
uv run python data/feature_engineering.py  # build model features (Elo, form, H2H, venue)
uv run python models/train_model.py       # train and save the XGBoost model
```

---

## Running with Docker

A `Dockerfile` is included for deploying just the backend API (e.g. to Hugging Face Spaces or any container host):

```bash
docker build -t cric-ai-backend .
docker run -p 8080:8080 cric-ai-backend
```

The API will be available at `http://localhost:8080`.

---

## API Overview

The FastAPI backend exposes these endpoints (see `backend/main.py`):

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Health check |
| `/metadata` | GET | List of valid team names and venues |
| `/stats?team1=&team2=` | GET | Recent form and head-to-head counts for two teams |
| `/predict/pre-match` | POST | Predict win probability given match details |
| `/team-analytics/{team}` | GET | Overall win rate and bat-first/bowl-first splits for a team |
| `/h2h-history?team1=&team2=` | GET | Head-to-head record and last 5 matches between two teams |
| `/elo-history/{team}` | GET | Elo rating over time for a team |

Once the backend is running, interactive API docs are available at `http://localhost:8000/docs`.

---

## Alternative: using pip without uv

If you'd prefer not to install uv, you can use the included `requirements.txt` instead:

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn backend.main:app --reload --port 8000    # terminal 1
streamlit run frontend/app.py                     # terminal 2
```

Note: `pyproject.toml` requires **Python 3.14+**. If you're using your own Python install, make sure it satisfies that requirement, or relax the `requires-python` constraint in `pyproject.toml` if you know your dependencies still work on an older version.

---

## Data Source

Match data is sourced from ball-by-ball T20 international JSON files (`t20s_json/`), aggregated into match-level records for feature engineering and model training.

## Authors

- Ammar Khalid
- Fateh Ali
- Abdullah Saleem

## License

This project is licensed under the [MIT License](LICENSE) — free to use, modify, and distribute, with attribution.

"""Supplied synthetic teaching example; complete your own extension separately."""

import json
import platform

import numpy as np
import pandas as pd
import sklearn
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score, f1_score
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def make_data(seed=42, rows=240):
    """Return artificial features/labels; missingness is added after label creation."""
    rng = np.random.default_rng(seed)
    score = rng.normal(size=rows)
    hours = rng.uniform(0, 8, size=rows)
    category = rng.choice(["A", "B", "C"], size=rows)
    margin = score + 0.35 * (hours - 4) + 0.6 * (category == "B")
    labels = (margin + rng.normal(scale=0.6, size=rows) > 0).astype(int)
    features = pd.DataFrame({"score": score, "hours": hours, "category": category})
    features.loc[rng.choice(rows, size=20, replace=False), "score"] = np.nan
    return features, pd.Series(labels, name="target")


def build_pipeline():
    numeric = Pipeline([
        ("impute", SimpleImputer(strategy="median")),
        ("scale", StandardScaler()),
    ])
    categorical = Pipeline([
        ("impute", SimpleImputer(strategy="most_frequent")),
        ("encode", OneHotEncoder(handle_unknown="ignore")),
    ])
    preprocess = ColumnTransformer([
        ("numeric", numeric, ["score", "hours"]),
        ("categorical", categorical, ["category"]),
    ], remainder="drop")
    return Pipeline([
        ("preprocess", preprocess),
        ("model", LogisticRegression(max_iter=1000, random_state=42)),
    ])


def main():
    features, labels = make_data()
    x_train, x_test, y_train, y_test = train_test_split(
        features, labels, test_size=0.25, random_state=42, stratify=labels
    )
    pipeline = build_pipeline()
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    scores = cross_val_score(pipeline, x_train, y_train, cv=cv, scoring="f1")
    pipeline.fit(x_train, y_train)
    predictions = pipeline.predict(x_test)
    summary = {
        "kind": "supplied synthetic teaching example",
        "seed": 42,
        "train_rows": len(x_train),
        "test_rows": len(x_test),
        "cv_f1_mean": float(scores.mean()),
        "cv_f1_std": float(scores.std()),
        "test_f1": float(f1_score(y_test, predictions)),
        "test_balanced_accuracy": float(balanced_accuracy_score(y_test, predictions)),
        "feature_names": pipeline.named_steps["preprocess"].get_feature_names_out().tolist(),
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "pandas": pd.__version__,
            "scikit_learn": sklearn.__version__,
        },
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

import pickle
from functools import lru_cache
from pathlib import Path

import pandas as pd
from django.conf import settings
from django.shortcuts import render

from .forms import TipPredictionForm


FEATURE_NAMES = ["total_bill", "sex", "smoker", "day", "time", "size"]
MODEL_PATH = settings.BASE_DIR / "ml_app" / "models" / "xgb_model.pkl"


@lru_cache(maxsize=1)
def _load_model():
    if not MODEL_PATH.is_file():
        raise FileNotFoundError(f"XGBoost model file was not found: {MODEL_PATH}")

    with MODEL_PATH.open("rb") as model_file:
        return pickle.load(model_file)


def home(request):
    form = TipPredictionForm(request.POST or None)
    prediction = None

    if request.method == "POST" and form.is_valid():
        features = pd.DataFrame([form.model_features()], columns=FEATURE_NAMES)
        prediction = float(_load_model().predict(features)[0])

    return render(
        request,
        "ml_app/home.html",
        {"form": form, "prediction": prediction},
    )


def how_it_works(request):
    return render(request, "ml_app/how_it_works.html")

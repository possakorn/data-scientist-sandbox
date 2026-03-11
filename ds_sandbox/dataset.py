"""Helpers to load built-in and generated example datasets."""
import numpy as np
import pandas as pd
from sklearn import datasets


def load_iris() -> pd.DataFrame:
    """Iris flower dataset (150 rows, 4 features + target)."""
    data = datasets.load_iris(as_frame=True)
    df = data.frame.copy()
    df["species"] = df["target"].map(dict(enumerate(data.target_names)))
    return df


def load_wine() -> pd.DataFrame:
    """Wine recognition dataset (178 rows, 13 features + target)."""
    data = datasets.load_wine(as_frame=True)
    df = data.frame.copy()
    df["class"] = df["target"].map(dict(enumerate(data.target_names)))
    return df


def load_diabetes() -> pd.DataFrame:
    """Diabetes progression dataset (442 rows, 10 features + target)."""
    data = datasets.load_diabetes(as_frame=True)
    return data.frame.copy()


def make_timeseries(n: int = 365, freq: str = "D", seed: int = 42) -> pd.DataFrame:
    """Generate a synthetic daily time-series with trend + seasonality + noise."""
    rng = np.random.default_rng(seed)
    dates = pd.date_range("2023-01-01", periods=n, freq=freq)
    trend = np.linspace(0, 10, n)
    seasonal = 5 * np.sin(2 * np.pi * np.arange(n) / 30)
    noise = rng.normal(0, 1, n)
    return pd.DataFrame({"date": dates, "value": trend + seasonal + noise})


def make_sales(seed: int = 42) -> pd.DataFrame:
    """Generate a synthetic sales DataFrame for practice."""
    rng = np.random.default_rng(seed)
    regions = ["North", "South", "East", "West"]
    products = ["Widget A", "Widget B", "Gadget X"]
    rows = []
    for month in range(1, 13):
        for region in regions:
            for product in products:
                rows.append({
                    "month": month,
                    "region": region,
                    "product": product,
                    "units_sold": int(rng.integers(50, 300)),
                    "unit_price": round(float(rng.uniform(9.99, 49.99)), 2),
                })
    df = pd.DataFrame(rows)
    df["revenue"] = df["units_sold"] * df["unit_price"]
    return df

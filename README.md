# Data Scientist Sandbox

A hands-on Python sandbox for data science practice — covering **NumPy**, **Pandas**, **PyTorch**, and **Plotly** with step-by-step notebooks and real example datasets.

## Quick Start

```bash
# 1. Create virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch JupyterLab
jupyter lab
```

## Practice Notebooks

| # | Notebook | Topics |
|---|----------|--------|
| 01 | `notebooks/01-numpy-fundamentals.ipynb` | Arrays, broadcasting, linear algebra, random |
| 02 | `notebooks/02-pandas-fundamentals.ipynb` | DataFrames, cleaning, groupby, merge, time series |
| 03 | `notebooks/03-plotly-visualization.ipynb` | Line, bar, scatter, heatmap, interactive charts |
| 04 | `notebooks/04-pytorch-basics.ipynb` | Tensors, autograd, simple neural network |

## Project Structure

```
├── README.md
├── requirements.txt          <- pip install -r requirements.txt
├── pyproject.toml
│
├── notebooks/                <- Step-by-step practice notebooks
│   ├── 01-numpy-fundamentals.ipynb
│   ├── 02-pandas-fundamentals.ipynb
│   ├── 03-plotly-visualization.ipynb
│   └── 04-pytorch-basics.ipynb
│
├── data/
│   ├── raw/                  <- Original datasets
│   ├── processed/            <- Cleaned/transformed data
│   └── external/             <- Third-party data
│
├── ds_sandbox/               <- Reusable helper modules
│   ├── __init__.py
│   ├── config.py
│   ├── dataset.py
│   ├── features.py
│   └── plots.py
│
├── models/                   <- Saved model weights
└── reports/figures/          <- Exported charts
```

## Stack

| Library | Version | Use |
|---------|---------|-----|
| `numpy` | >=1.24 | Numerical computing |
| `pandas` | >=2.0 | Data manipulation |
| `torch` | >=2.0 | Deep learning |
| `plotly` | >=5.0 | Interactive visualization |
| `scikit-learn` | >=1.3 | ML utilities & datasets |
| `scipy` | >=1.10 | Scientific computing |
| `seaborn` | latest | Statistical plots |

---
*Built with [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/)*

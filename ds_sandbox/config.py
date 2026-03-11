from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
MODELS_DIR = ROOT / "models"
REPORTS_DIR = ROOT / "reports" / "figures"

for _d in [RAW_DIR, PROCESSED_DIR, MODELS_DIR, REPORTS_DIR]:
    _d.mkdir(parents=True, exist_ok=True)

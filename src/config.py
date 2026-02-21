from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data"
DATASET_DIR = DATA_DIR / "asl_yolo"
DATA_YAML = DATASET_DIR / "data.yaml"

MODELS_DIR = PROJECT_ROOT / "models"
BASE_MODELS_DIR = MODELS_DIR / "base"
TRAINED_MODELS_DIR = MODELS_DIR / "trained"
BEST_MODEL = TRAINED_MODELS_DIR / "best.pt"

RUNS_DIR = PROJECT_ROOT / "runs"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
PRED_DIR = OUTPUTS_DIR / "predictions"

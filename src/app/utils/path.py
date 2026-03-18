from pathlib import Path

def find_project_root_from_pyproject():
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / "pyproject.toml").exists():
            return parent
    raise RuntimeError("pyproject.toml not found")
        
PROJECT_ROOT = find_project_root_from_pyproject()
SAMPLE_DATA_PATH = PROJECT_ROOT / "storage" / "yohou_43056.csv"
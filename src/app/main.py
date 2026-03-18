from src.app.utils.path import SAMPLE_DATA_PATH
from src.app.services.risk import load_wbgt

def main():
    print(load_wbgt(SAMPLE_DATA_PATH))

if __name__ == "__main__":
    main()
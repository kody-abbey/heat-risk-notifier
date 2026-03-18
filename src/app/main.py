from src.app.utils.path import SAMPLE_DATA_PATH
from src.app.services.risk import load_wbgt, evaluate_risk

def main():
    data_list = load_wbgt(SAMPLE_DATA_PATH)
    for d in data_list:
        risk = evaluate_risk(d.value)
        print(d.time, d.value, risk.value)


if __name__ == "__main__":
    main()
import csv
from datetime import datetime, timedelta
from src.app.config import WBGT_THRESHOLDS
from src.app.models import RiskLevel, WBGTData


def load_wbgt(path):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f, skipinitialspace=True)
        # Time
        header = next(reader)
        times = header[2:]
        print(times)

        row = next(reader)
        values = row[2:]
        print(values)

        result = []

        for t, v in zip(times, values):
            parsed = parse_row(t, v)
            if parsed:
                result.append(parsed)

        return result

def parse_row(t: str, v: str):
    t = t.strip()
    v = v.strip()

    if not t or not v:
        return None

    if len(t) != 10 or not t.isdigit():
        return None

    try:
        value = int(v) / 10
    except ValueError:
        return None

    base = datetime.strptime(t[:8], "%Y%m%d")
    hour = int(t[8:10])
    dt = base + timedelta(hours=hour)

    return WBGTData(time=dt, value=value)

def evaluate_risk(value: float) -> RiskLevel:
    for level, threshold in WBGT_THRESHOLDS:
        if value >= threshold:
            return level
    return RiskLevel.SAFE
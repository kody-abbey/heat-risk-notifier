from enum import Enum
from dataclasses import dataclass
from datetime import datetime

class RiskLevel(Enum):
    DANGER = "danger"
    SEVERE = "severe"
    WARNING = "warning"
    CAUTION = "caution"
    SAFE = "safe"

@dataclass
class WBGTData:
    time: datetime
    value: float
from src.app.models import RiskLevel
# WBGT
WBGT_THRESHOLDS = [
    (RiskLevel.DANGER, 31),
    (RiskLevel.SEVERE, 28),
    (RiskLevel.WARNING, 25),
    (RiskLevel.CAUTION, 21),
]

import enum
from datetime import date


class RepresentativeType(enum.Enum):
    REGULAR = "regular"
    HEALTH_AND_SAFETY = "health-and-safety"
    EQUALITIES = "equalities"

class Representative:
    representative_type: RepresentativeType
    role_start_date: date
    handles_cases: bool


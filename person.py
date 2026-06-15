import enum
from datetime import date


class MembershipStatus(enum.Enum):
    # different types of membership in Prospect
    NON_MEMBER = "non-member"
    REPRESENTATIVE = "representative"
    STANDARD_MEMBER = "standard-member"
    FULL_TIME = "full-time"

    # find a way to add membership start date

class Assessment(enum.Enum):
    PRO = "pro"
    NEUTRAL = "neutral"
    ANTI_UNION = "anti-union"

class Person:
    identifier: int # unique identifier
    name: str
    start_date: date
    membership_status: MembershipStatus
    assessment: Assessment
    # the people to whom the Person is connected. Score given to show amicability
    # -5 = strong opponent
    # 0 = neutral
    # 5 = strong friend
    colleagues: dict[Person, int]
    notes: list[str]
    last_contacted = date


    def __init__(self, identifier: int, name: str, start_date: date, assessment: Assessment):
        self.identifier = identifier
        self.name = name
        self.start_date = start_date
        self.assessment = assessment
        self.colleagues = {}
        self.notes = []

    def is_in_union(self):
        return self.membership_status is not MembershipStatus.NON_MEMBER

    def add_note(self, note: str) -> str:
        self.notes.append(note)
        return note

    def add_colleague(self, colleague: Person, score: int):
        self.colleagues[colleague] = score


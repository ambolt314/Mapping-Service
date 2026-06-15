import enum
from datetime import date

from people.assessment import Assessment
from people.membership import Membership

class Person:
    identifier: int # unique identifier
    name: str
    workplace_start_date: date
    workplace_end_date: date | None
    membership: Membership | None
    assessment: Assessment
    # the people to whom the Person is connected. Score given to show amicability
    # -5 = strong opponent
    # 0 = neutral
    # 5 = strong friend
    colleagues: dict[Person, int]
    notes: list[str]
    last_contacted = date


    def __init__(self, identifier: int, name: str, workplace_start_date: date, assessment: Assessment):
        self.identifier = identifier
        self.name = name
        self.workplace_start_date = workplace_start_date
        self.assessment = assessment
        self.colleagues = {}
        self.notes = []

    def get_start_date_difference(self):
        if self.is_in_union() and self.membership:
            return self.workplace_start_date - self.membership.start_date
        else:
            return 0

    def is_current_employee(self):
        return self.workplace_end_date is None

    def is_in_union(self):
        try:
            return self.membership is not None
        except AttributeError:
            return False

    def add_note(self, note: str) -> str:
        self.notes.append(note)
        return note

    def add_colleague(self, colleague: Person, score: int):
        self.colleagues[colleague] = score


from datetime import date

from people.membership import Membership


class Person:
    identifier: int
    name: str
    workplace_start_date: date
    workplace_end_date: date | None
    membership: Membership | None


    def __init__(self, identifier: int, name: str, workplace_start_date: date):
        self.identifier = identifier
        self.name = name
        self.workplace_start_date = workplace_start_date


    def get_start_date_difference(self):
        if self.is_in_union() and self.membership:
            return self.workplace_start_date - self.membership.membership_start_date
        else:
            return 0

    def is_current_employee(self):
        return self.workplace_end_date is None

    def is_in_union(self):
        try:
            return self.membership is not None
        except AttributeError:
            return False

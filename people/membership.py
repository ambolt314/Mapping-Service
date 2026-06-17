import enum
from datetime import date

from people.union_sentiment import UnionSentiment
from people.representative import Representative
from people.union_strength import UnionStrength

class Membership:
    membership_id: int # unique identifier for Prospect members
    branch: str = "UK Research and Innovation"
    membership_start_date: date
    membership_comments: list[str] = []
    email_address = str
    union_sentiment: UnionSentiment | None
    union_strength: UnionStrength | None
    representative: Representative | None

    def __init__(self, membership_id: int, email_address: str, branch: str = "UK Research and Innovation", membership_start_date: date = date.today()):
        self.membership_id = membership_id
        self.branch = branch
        self.membership_start_date = membership_start_date
        self.email_address = email_address

    def add_membership_comment(self, comment: str):
        self.membership_comments.append(comment)

    def is_representative(self):
        return self.representative is not None

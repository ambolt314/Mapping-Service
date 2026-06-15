import enum
from datetime import date


class MembershipType(enum.Enum):
    # different types of membership in Prospect
    REPRESENTATIVE = "representative"
    STANDARD_MEMBER = "standard-member"
    FULL_TIME = "full-time"

class Membership:
    membership_id: int # unique identifier for Prospect members
    membership_type: MembershipType
    start_date: date
    previous_membership: Membership | None
    membership_comments: list[str] = []

    def __init__(self, membership_type: MembershipType, start_date: date = date.today(), previous_membership: Membership | None = None):
        self.membership_type = membership_type
        self.start_date = start_date
        self.previous_membership = previous_membership

    def add_membership_comment(self, comment: str):
        self.membership_comments.append(comment)

# Mapping Service

This is a new service intended to help unionisation efforts.
The service was designed for use within Prospect, though this code can be forked for more specialised usage.

## Person
This describes a `Person` of interest to Prospect, whether they are affilated with the union.

### Identifier
The unique identifier for the Mapping Service.

### Name
The name of the `Person`.

### Email address
The email address of the `Person`, to be used to contact the `Person`

### Workplace start date
The date the `Person` started their workplace.

### Workplace end date
The date the `Person` ended their workplace.
For current employees, this will be `None`.

### Membership
For those with membership in the union, they will be given a `Membership`.

This contains the following information:
- `membership_id`: the unique identifier from Prospect
- `membership_type`: the type of union membership
- `start_date`: the date the membership started
- `previous_membership`: the previous membership
- `membership_comments`: comments specifically to the membership

### Assessment
The attitude towards unions from the `Person`

The following assessment types are supported:
- `PRO`
- `NEUTRAL`
- `ANTI_UNION`

### Colleagues
These are people who are connected to the `Person`. This means anyone with whom the `Person` is in some kind of contact.

Each `Person` has a score, ranging from `-5` to `5`. This is an assessment from the `Person` themselves about the degree of friendliness towards the given colleague.
- `-5` is a strong opponent
- `0` is neutral
- `5` is a strong friend

### Notes
Any notes about the `Person`.

### Last contacted
The date that the `Person` was last contacted.

### `get_start_date_difference()`
The difference between the workplace start date and the union membership start date.

### `is_current_employee()`
Returns `True` if the `Person` is currently in their workplace.

### `is_in_union()`
Returns `True` if the `Person` is in a union.

### `add_note()`
Adds a note to the `Person`.

### `add_colleague()`
Adds a colleague to the `Person`.

---

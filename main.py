# This is a sample Python script.
from people.worker import Person

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

people: list[Person] = []


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def get_person_by_identifier(identifier: int):
    results = list(filter(lambda person: person.identifier == identifier, people))
    if len(results) != 1:
        raise ValueError(f"Error retrieving person with identifier {identifier}, found {len(results)}")
    return results[0]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

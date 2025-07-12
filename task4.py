from datetime import datetime

def get_upcoming_birthdays(users: list) -> list:
    birthdays = []

    today = datetime.today().date()

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        birthday_this_year = datetime(today.year, birthday.month, birthday.day).date()

        if birthday_this_year > today:
            next_birthday = birthday_this_year
        else:
            next_birthday = birthday_this_year.replace(year=today.year + 1)

        if (next_birthday - today).days < 7:
            birthdays.append(user)

    return birthdays

users = [
    {"birthday": "1999.12.22", "name": "Test1"},
    {"birthday": "1999.01.22", "name": "Test2"},
    {"birthday": "1999.07.22", "name": "Test3"},
    {"birthday": "1999.11.22", "name": "Test4"},
    {"birthday": "1999.02.22", "name": "Test5"},
    {"birthday": "1999.07.19", "name": "Test6"},
    {"birthday": "1999.07.18", "name": "Test7"},
]

print(get_upcoming_birthdays(users))
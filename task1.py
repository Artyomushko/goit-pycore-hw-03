import datetime

def get_days_from_today(date: str) -> int:
    try:
        formatted_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid format")
        return 0
    difference = formatted_date - datetime.date.today()
    return difference.days

print(get_days_from_today("2021-10-09")) # past
print(get_days_from_today("2026-10-09")) # future
print(get_days_from_today("2026-13-09")) # invalid
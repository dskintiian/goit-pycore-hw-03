"""
Завдання 4
"""
from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list) -> list:
    upcoming_birthdays = []
    for user in users:
        try:
            birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").replace(year=datetime.today().year).date()
        except ValueError as e:
            print(f"Invalid birthdate provided for {user['name']}, use YYYY.MM.DD format")
            continue

        if birthday < datetime.today().date():
            birthday.replace(year=datetime.today().year + 1)

        if (datetime.today().date() - birthday).days < 7:
            if birthday.weekday() >= 5:
                add_days = 7 - birthday.weekday()
                birthday += + timedelta(days=add_days)

            upcoming_birthdays.append({"name": user["name"], "congratulation_date": birthday.strftime("%Y.%m.%d")})

    return upcoming_birthdays


input_users = [
    # From task description
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    # Sunday - today
    {"name": "Hope Shelton", "birthday": "2020.07.07"},
    # Before today
    {"name": "Kathy Mathews", "birthday": "2004.05.02"},
    # Next Saturday
    {"name": "Raiden Arias", "birthday": "1995.07.13"},
    # Valid
    {"name": "Harper Lawson", "birthday": "1996.07.09"},
    # Invalid date format
    {"name": "Harper Lawson", "birthday": "02-07-1994"},
]

upcoming_birthdays = get_upcoming_birthdays(input_users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

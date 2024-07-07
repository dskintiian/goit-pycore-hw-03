"""
Завдання 1
"""
from datetime import datetime


def get_days_from_today(date: str) -> int or None:
    try:
        difference = datetime.now() - datetime.strptime(date, '%Y-%m-%d')
        return difference.days
    except ValueError as e:
        print(f"Invalid date provided, use YYYY-MM-DD format for input date.\n### {e} ###")


# past
print(get_days_from_today("2021-10-09"))
# today
print(get_days_from_today("2024-07-07"))
# future
print(get_days_from_today("2026-04-12"))
# invalid
print(get_days_from_today("2026-02-55"))
print(get_days_from_today("yesterday"))
print(get_days_from_today("Python is a programming language"))

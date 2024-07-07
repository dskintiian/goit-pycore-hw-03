"""
Завдання 1
"""
from datetime import datetime


def get_days_from_today(date: str):
    difference = datetime.now() - datetime.strptime(date, '%Y-%m-%d')

    return difference.days


# past
print(get_days_from_today("2021-10-09"))
# today
print(get_days_from_today("2024-07-07"))
# future
print(get_days_from_today("2026-04-12"))

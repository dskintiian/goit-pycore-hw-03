"""
Завдання 2
"""
from random import sample


def get_numbers_ticket(min: int, max: int, quantity: int):
    try:
        if min < 1:
            raise ValueError("First argument must be greater than or equal to 1.")
        if max > 1000:
            raise ValueError("Second argument must be less than or equal to 1000.")
        if quantity >= max:
            raise ValueError("Third argument must be less than or equal to max.")

        numbers = sample(range(min, max), k=quantity)
        numbers.sort()

        return numbers
    except ValueError as e:
        print(e)


# valid
print(get_numbers_ticket(1,1000,7))
# invalid first argument
print(get_numbers_ticket(-1,10,2))
# invalid second argument
print(get_numbers_ticket(10,1001,5))
# invalid third argument
print(get_numbers_ticket(1,10,10))

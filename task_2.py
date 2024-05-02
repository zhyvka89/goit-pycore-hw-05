import re
from typing import Callable


def generator_numbers(text: str):
    numbers =  re.findall(r'\b([1-9][0-9]*?[0-9]\.[0-9]+)\b', text)
    for num in numbers:
        yield num
    

def sum_profit(text: str, func: Callable):
    total = 0
    for num in func(text):
        total += float(num)
    return total



text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

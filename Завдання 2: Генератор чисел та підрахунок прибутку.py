import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r'\d+\.\d+'
    matches = re.findall(pattern, text)
    for match in matches:
        yield float(match)

def sum_profit(text: str, func: Callable):
    total = 0
    for number in func(text):
        total += number
    return total

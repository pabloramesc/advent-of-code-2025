import numpy as np


def max_joltage(bank: int) -> int:
    digits = [int(d) for d in str(bank)]
    idx1 = np.argmax(digits[:-1])
    idx2 = np.argmax(digits[idx1 + 1 :]) + idx1 + 1
    d1, d2 = digits[idx1], digits[idx2]
    return d1 * 10 + d2


with open("day3_input.txt", "r") as file:
    txt = file.read()
    banks = txt.split()


total = 0
for bank in banks:
    total += max_joltage(int(bank))

print("Total output joltage:", total)

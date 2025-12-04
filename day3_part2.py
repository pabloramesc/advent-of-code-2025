def max_joltage(bank: int) -> int:
    digits = list(str(bank))
    while len(digits) > 12:
        candidates = []
        for k in range(len(digits)):
            candidate_digits = digits.copy()
            candidate_digits.pop(k)
            candidate_num = int("".join(candidate_digits))
            candidates.append(candidate_num)
        best = max(candidates)
        digits = list(str(best))
    return int("".join(digits))


with open("day3_input.txt", "r") as file:
    txt = file.read()
    banks = txt.split()

total = 0
for bank in banks:
    total += max_joltage(int(bank))

print("Total output joltage:", total)

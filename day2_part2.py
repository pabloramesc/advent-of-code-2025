from day2_part1 import range_to_nums


def is_invalid_id(num: int) -> bool:
    digits = str(num)
    size = len(digits)
    for k in range(1, size // 2 + 1):
        pattern = digits[:k]
        times = size // len(pattern)
        candidate = pattern * times
        if candidate == digits:
            return True
    return False


with open("day2_input.txt", "r") as file:
    txt = file.read()
    ranges = txt.strip().split(",")

invalid_ids = set()
for rang in ranges:
    nums = range_to_nums(rang)
    for num in nums:
        if is_invalid_id(num):
            invalid_ids.add(num)

print("Sum of invalid IDs:", sum(invalid_ids))

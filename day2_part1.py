def range_to_nums(rang: str) -> list[int]:
    start, stop = rang.split("-")
    return list(range(int(start), int(stop) + 1))


def is_invalid_id(num: int) -> bool:
    digits = str(num)
    if len(digits) % 2:
        ValueError("IDs must be numbers with even number of digits!")
    mid = len(digits) // 2
    part1 = digits[:mid]
    part2 = digits[mid:]
    return part1 == part2


if __name__ == "__main__":
    with open("day2_input.txt", "r") as file:
        txt = file.read().strip()
        ranges = txt.split(",")

    invalid_ids = set()
    for rang in ranges:
        nums = range_to_nums(rang)
        for num in nums:
            if is_invalid_id(num):
                invalid_ids.add(num)

    print("Sum of invalid IDs:", sum(invalid_ids))

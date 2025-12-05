def process_database(txt: str):
    lines = txt.splitlines()
    idx = lines.index("")
    ranges = lines[:idx]
    ids = lines[idx + 1 :]
    return ranges, ids


def is_fresh(i: int, ranges: list[str]):
    for rang in ranges:
        start, stop = rang.split("-")
        if int(start) <= i <= int(stop):
            return True
    return False


if __name__ == "__main__":

    with open("day5_input.txt", "r") as file:
        txt = file.read()

    ranges, ids = process_database(txt)

    count = 0
    for i in ids:
        if is_fresh(int(i), ranges):
            count += 1
            print(f"Ingredient {i} is fresh")
        else:
            print(f"Ingredient {i} is spoiled")

    print(f"There are {count} fresh ingredients")

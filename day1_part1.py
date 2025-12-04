def rotation_to_displacement(rot: str):
    if rot[0] not in "LR":
        raise ValueError("Not valid rotation!")
    direction = +1 if rot[0] == "R" else -1
    distance = int(rot[1:])
    return direction, distance


if __name__ == "__main__":
    dial_size = 100

    with open("day1_input.txt", "r") as file:
        rotations = [line.strip() for line in file]

    dial, count = 50, 0
    for rot in rotations:
        dir, dist = rotation_to_displacement(rot)
        dial = (dial + dist * dir) % dial_size
        count += 1 if dial == 0 else 0
        
    print(f"Number of times left pointing at zero: {count}")

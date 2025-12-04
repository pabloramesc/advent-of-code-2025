from day1_part1 import rotation_to_displacement

dial_size = 100

with open("day1_input.txt", "r") as file:
    rotations = [line.strip() for line in file]

dial, count = 50, 0
for rot in rotations:
    dir, disp = rotation_to_displacement(rot)

    if dir > 0:
        dist_to_zero = 100 - dial
    elif dir < 0:
        dist_to_zero = dial

    if dist_to_zero == 0:
        dist_to_zero = dial_size

    if disp >= dist_to_zero:
        remaining_dist = disp - dist_to_zero
        count += remaining_dist // dial_size + 1

    dial = (dial + disp * dir) % dial_size


print(f"Number of times crossed zero: {count}")

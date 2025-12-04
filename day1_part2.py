from day1_part1 import rotation_to_displacement

dial_size = 100

with open("day1_input.txt", "r") as file:
    rotations = [line.strip() for line in file]

dial, count = 50, 0
for rot in rotations:
    dir, pos = rotation_to_displacement(rot)
    for k in range(pos):
        dial += dir
        if dial > 99:
            dial = 0
        if dial < 0:
            dial = 99
        if dial == 0:
            count += 1
    
print(f"Number of times crossed zero: {count}")

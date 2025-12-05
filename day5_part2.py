from day5_part1 import process_database

def range_to_tuple(rang: str) -> tuple[int, int]:
    a, b = rang.split("-")
    return int(a), int(b)


with open("day5_input.txt", "r") as file:
    txt = file.read()

ranges, _ = process_database(txt)

# Convert ranges to a list of tuples
ranges = [range_to_tuple(r) for r in ranges]

# Sort ranges by start value
ranges.sort(key=lambda r: r[0])


pos = 0
while pos < len(ranges) - 1:
    r1 = ranges[pos]
    r2 = ranges[pos+1]
    
    # If r1 overlaps with r2, merge r1 and r2 into r
    if r1[1] + 1 >= r2[0] or r1[0] == r2[0]:
        stop = max(r1[1], r2[1])
        r = (r1[0], stop)
        ranges.pop(pos)
        ranges.pop(pos)
        ranges.insert(pos, r)
        continue
    
    else:
        pos += 1
        
total = 0
for r in ranges:
    total += r[1] - r[0] + 1

print(f"There are {total} fresh ingredients according to ID ranges.")
with open("input/day1.txt") as f:
    data = f.readlines()


currcalories = 0
highestcalories = 0
top2 = 0
top3 = 0

for line in data:
    if line == "\n":
        if highestcalories < currcalories:
            highestcalories = currcalories
        elif top2 < currcalories:
            top2 = currcalories
        elif top3 < currcalories:
            top3 = currcalories

        currcalories = 0
    else:
        currcalories += int(line.strip("\n"))

print(f"Part 1: {highestcalories}")

print(f"Part 2: {highestcalories + top2 + top3}")
input()
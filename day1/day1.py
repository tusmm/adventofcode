"""
total each line then compare to the calorie counter
"""

calories = []

with open("input1.txt", 'r') as f:
    elfCalorie = 0
    for line in f:
        if line == '\n':
            calories.append(elfCalorie)
            elfCalorie = 0
        else:
            elfCalorie += int(line.strip())

top3Cal = sorted(calories)[-3:]

total = 0
for cal in top3Cal:
    total += cal

print(total)

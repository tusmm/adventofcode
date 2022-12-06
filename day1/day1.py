
mostCalories = 0;


with open("input1.txt", 'r') as f:
    elfCalorie = 0
    for line in f:
        if line == '\n':
            if mostCalories < elfCalorie:
                mostCalories = elfCalorie
                elfCalorie = 0
                continue
        elfCalorie += int(line)

print(mostCalories)


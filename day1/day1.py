"""
total each line then compare to the calorie counter
"""

mostCalories = 0;

with open("input1.txt", 'r') as f:
    elfCalorie = 0
    for line in f:
        if line == '\n':
            if mostCalories < elfCalorie:
                mostCalories = elfCalorie
            elfCalorie = 0
        else:
            elfCalorie += int(line.strip())
        
print(mostCalories)

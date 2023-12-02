# possible combinations
scores = {
    'A X': 3 + 1,
    'A Y': 6 + 2,
    'A Z': 0 + 3,
    'B X': 0 + 1,
    'B Y': 3 + 2,
    'B Z': 6 + 3,
    'C X': 6 + 1,
    'C Y': 0 + 2,
    'C Z': 3 + 3,
}

# options
op = {
    'A': 1,
    'B': 2,
    'C': 3
}
op2 = {
    0: 'A',
    1: 'B',
    2: 'C'
}

# loss
# 1, 2
# 2, 0
# 3, 1

# win
# 1, 1
# 2, 2
# 3, 0

score = 0
with open("input.txt", "r") as f:
    for line in f:
        strat = line[2]
        if strat == 'X':
            # lose
            score += op[op2[(op[line[0]] + 1) % 3]]
        elif strat == 'Y':
            # draw
            score += (op[line[0]]) + 3
        elif strat == 'Z':
            # win
            score += (op[op2[(op[line[0]]) % 3]]) + 6
            
print(score)
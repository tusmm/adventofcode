# get two digits from the string and then add them

def get_calibration_val(line):
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num = ''
    for ch in line:
        if ch.isdigit():
            num += ch
            break
    for ch in line[::-1]:
        if ch.isdigit():
            num += ch
            break
    return int(num)

def calc_all(filename):
    total = 0
    with open(filename,'r') as f:
        for line in f:
            total += get_calibration_val(line)
    return total

print(calc_all('input.txt'))
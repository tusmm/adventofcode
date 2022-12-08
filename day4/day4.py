total = 0

with open("input.txt", "r") as f:
    for line in f:
        temp = line.strip().split(",")

        num = []

        for x in temp:
            temp2 = x.split("-")
            for i in temp2:
                num.append(i)

        if int(num[0]) <= int(num[2]) and int(num[1]) >= int(num[3]):
            total += 1
        elif int(num[2]) <= int(num[0]) and int(num[3]) >= int(num[1]):
            total += 1

print(total)
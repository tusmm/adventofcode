# day3 part 1
# total = 0

# with open("input.txt", "r") as f:
#     for line in f:
#         front = line[:len(line)//2]
#         end = line[len(line)//2:len(line)]
#         comm = ''
#         for ch in front:
#             if ch in end:
#                 comm = ch
#         if comm.isupper():
#             # is uppercase
#             total += ord(comm) - 38
#         else:
#             # is lowercase
#             total += ord(comm) - 96

# print(total)

# day3 part2
total = 0
totalTriplets = 0
with open("input.txt", "r") as f:
    elf3 = []
    count = 0
    for line in f:
        if totalTriplets == 99 and count == 2:
            elf3.append(line.strip())
            count += 1
        if count < 3:
            elf3.append(line.strip())
            count += 1
        else:
            comm = ''
            for ch in elf3[0]:
                if ch in elf3[1] and ch in elf3[2]:
                    comm = ch
                    if comm.isupper():
                        # is uppercase
                        total += ord(comm) - 38
                    else:
                        # is lowercase
                        total += ord(comm) - 96
                    elf3.clear()
                    break
            elf3.clear()
            count = 1
            elf3.append(line)
            totalTriplets += 1

print(totalTriplets)
print(total)


# total = 0
# elf3 = ["vJrwpWtwJgWrhcsFMMfFFhFp",
# "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
# "PmmdzqPrVvPwwTWBwg"]
# for line in elf3:
#     if len(elf3) != 3:
#         elf3.append(line)
#         print(elf3)
#     else:
#         for ch in elf3[0]:
#             if ch in elf3[1] and ch in elf3[2]:
#                 if ch.isupper():
#                     # is uppercase
#                     total += ord(ch) - 38
#                 else:
#                     # is lowercase
#                     total += ord(ch) - 96
#                 elf3 = ["wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
#                         "ttgJtRGJQctTZtZT",
#                         "CrZsJsPPZsGzwwsLwLmpwMDw"]
#                 break

# print(total)
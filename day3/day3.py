total = 0  

with open("input.txt", "r") as f:
    for line in f:
        front = line[:len(line)//2]
        end = line[len(line)//2:len(line)]
        comm = ''
        for ch in front:
            if ch in end:
                comm = ch
        if comm.isupper():
            # is uppercase
            total += ord(comm) - 38
        else:
            # is lowercase
            total += ord(comm) - 96

print(total)
x = 0 # forward
y = 0 # depth


with open("day2/input.txt") as f:
    lines = f.readlines()

    for l in lines:
        dir = l.split()[0]
        nb = int(l.split()[1])

        if dir == "forward":
            x += nb
        elif dir == "up":
            y -= nb
        else:
            y += nb


x2 = 0 
y2 = 0
aim = 0
with open("day2/input.txt") as f:
    lines = f.readlines()
    for l in lines:
        dir = l.split()[0]
        nb = int(l.split()[1])

        if dir == "forward":
            x2 += nb
            y2 += aim * nb 
        elif dir == "up":
            aim -= nb
            #y2 -= nb
        else:
            aim += nb
            #y2 += nb

print( "pb1 {0}".format(x*y))
print( "pb2 {0}".format(x2*y2))

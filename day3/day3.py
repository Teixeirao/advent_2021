# day4 refactoring
def filter(pos, value, ina):
    l = 0
    for l in list(ina):
        if l[pos] != value:
            ina.remove(l)
    return ina

# Used on day3
def filter_orig(pos, value, ina):
    l = 0
    while l < len(ina):
        if ina[l][pos] != value:
            ina.pop(l)
            l -= 1
        l +=  1
    return ina

def more1(ina, pos):
    cnt = 0
    size = len(ina)
    for l in ina:
        if l[pos] == "1":
           cnt += 1
    return (cnt >= (size/2))

cnt1 = [0,0,0,0,0,0,0,0,0,0,0,0]
cnt0 = [0,0,0,0,0,0,0,0,0,0,0,0]

with open("day3/input.txt") as f:
    lines = f.readlines()

for l in lines:
    for i in range(0,len(cnt1)):
        if l[i] == '1':
            cnt1[i] += 1
        else:
            cnt0[i] += 1

gamma_str = ""
epsilon_str = ""
for i in range(0,len(cnt1)):
    if cnt1[i] > cnt0[i]:
        gamma_str += "1"
        epsilon_str += "0"
    else:
        gamma_str += "0"
        epsilon_str += "1"


gama = int(gamma_str, 2)
epsilon = int(epsilon_str, 2)

print("pb1 {0}".format(gama * epsilon))

inarray = lines.copy()
for pos in range(0,12):
    m1 = more1(inarray,pos)
    if m1:
        inarray = filter(pos,'1',inarray)
    else:
        inarray = filter(pos,'0',inarray)

    if len(inarray) == 1:
        break

oxy = int(inarray[0],2)


inarray = lines.copy()
for pos in range(0,12):
    m1 = more1(inarray,pos)
    if m1:
        inarray = filter(pos,'0',inarray)
    else:
        inarray = filter(pos,'1',inarray)
    
    if len(inarray) == 1:
        break

co2 = int(inarray[0],2)

print("pb2 {0}".format(oxy*co2))

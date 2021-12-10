
input_loc = "day10/input.txt"

with open(input_loc) as f:
    lines = f.readlines()


points = {
    ")" : 3,
    "]" : 57,
    "}" : 1197,
    ">" : 25137
}

op = ["(","[","{","<"]
cl = [")", "]", "}", ">"]

match = {
    ")" :  "(",
    "]" :  "[",
    "}" :  "{",
    ">" :  "<"
}

match_close = {
    "(" :  ")" ,
    "[" :  "]" ,
    "{" :  "}" ,
    "<" :  ">" 
}

score = 0
corrupted_line = []
for l in lines:
    #print('ici')
    lifo = []
    for i in range(len(l.strip())):
        if l[i] in op:
            lifo.append(l[i])
        else:
            if lifo[-1] != match[l[i]]:
                #print("corrupted")
                #print(l)
                #print(lifo)
                #print(l[i])
                #print(i)
                corrupted_line.append(l)
                score += points[l[i]]
                break
            else:
                lifo.pop(len(lifo)-1)

print(score)

points_complete = {
    ")" : 1,
    "]" : 2,
    "}" : 3,
    ">" : 4
}

scores = []
for l in lines:
    #print('ici')
    lifo = []
    if l in corrupted_line:
        continue
    for i in range(len(l.strip())):
        if l[i] in op:
            lifo.append(l[i])
        else:
            lifo.pop(len(lifo)-1)
    
    score = 0
    while len(lifo) != 0:
        score *= 5
        score += points_complete[match_close[lifo[-1]]]
        lifo.pop(len(lifo)-1)
        #print(lifo)
        #print(score)
    scores.append(score)

scores.sort()
print(scores[int(len(scores)/2)])
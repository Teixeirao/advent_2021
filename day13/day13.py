input_loc = "day13/input.txt"
psize = 2000

with open(input_loc) as f:
    lines = f.readlines()

paper_orig = [[False] * psize for i in range(psize)]
fold_along = []
for l in lines:
    if "fold" in l:
        la = l.split()
        dir = la[2].split("=")[0]
        nb = int(la[2].split("=")[1])

        fold_along.append([dir,nb])
    elif l.strip() != "":
        la = l.split(",")
        x = int(la[0])
        y = int(la[1])
        paper_orig[y][x] = True

#v1

paper = paper_orig.copy()
if fold_along[0][0] == "y":
    split = fold_along[0][1]
    for j in range(split+1,psize-split):
        rj = split - (j-split)
        #print(rj)
        for i in range(psize):
            if rj >= 0:
                paper[rj][i] = paper[rj][i] | paper[j][i]
            paper[j][i] = False

if fold_along[0][0] == "x":
    split = fold_along[0][1]
    for i in range(split+1,psize-split):
        ri = split - (i-split)
        #print(ri)
        for j in range(psize):
            if ri >= 0:
                paper[j][ri] = paper[j][ri] | paper[j][i]
            paper[j][i] = False

cnt = 0
for j in range(psize):
    for i in range(psize):
        if paper[j][i]:
            cnt += 1

print(cnt)


#v2
paper = paper_orig.copy()
for fold in fold_along:
    if fold[0] == "y":
        split = fold[1]
        for j in range(split+1,len(paper)-split+1):
            rj = split - (j-split)
            #print(rj)
            for i in range(len(paper[j])):
                if rj >= 0:
                    #print(rj)
                    paper[rj][i] = paper[rj][i] | paper[j][i]
                paper[j][i] = False
                #paper.pop(j)
                #print("ICI")

    if fold[0] == "x":
        split = fold[1]
        for i in range(split+1,len(paper[0])-split+1):
            ri = split - (i-split)
            #print(ri)
            for j in range(psize):
                if ri >= 0:
                    paper[j][ri] = paper[j][ri] | paper[j][i]
                    #paper[j].pop(i) 
                paper[j][i] = False
    #print("la")
    #for j in range(psize):
    #    for i in range(psize):
    #        print("{0}".format("#" if paper[j][i] else "."), end="")
    #    print("")

#print(paper)
for j in range(0,20):
    for i in range(0,60):
        print("{0}".format("#" if paper[j][i] else "."), end="")
    print("")

#print(paper)


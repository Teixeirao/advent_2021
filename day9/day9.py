
import seaborn as sns
import matplotlib.pyplot as plt

with open("day9/input.txt") as f:
    lines = f.readlines()

heightmap = [[0] * len(lines[0].strip()) for j in range(len(lines))]

for j in range(len(lines)):
    l = lines[j].strip()
    for i in range(len(l)):
        heightmap[j][i] = int(lines[j][i])


print(heightmap)

heightmap_low = [[False] * len(lines[0].strip()) for j in range(len(lines))]
low_index = []

for j in range(len(heightmap)):
    for i in range(len(heightmap[j])):
        up = heightmap[j-1][i] if j-1 >= 0 else 100
        down = heightmap[j+1][i] if j+1 < len(heightmap) else 100
        left = heightmap[j][i-1] if i-1 >= 0 else 100
        right = heightmap[j][i+1] if i+1 < len(heightmap[j]) else 100

        if heightmap[j][i] < up and heightmap[j][i] < down and heightmap[j][i] < left and heightmap[j][i] < right:
            heightmap_low[j][i] = True
            low_index.append([j,i])

print(heightmap_low)

sum = 0
for j in range(len(heightmap)):
    for i in range(len(heightmap[j])):
        if  heightmap_low[j][i]:
            sum += heightmap[j][i] + 1

print(sum)

heightmap_bassin = [[-1] * len(lines[0].strip()) for j in range(len(lines))]

def add_to_bassin(j,i,id):
    size = 0
    if heightmap[j][i] != 9 and heightmap_bassin[j][i] == -1:
        heightmap_bassin[j][i] = id
        size += 1
        if j-1 >= 0:
            size += add_to_bassin(j-1,i,id)
        if j+1 < len(heightmap):
            size += add_to_bassin(j+1,i,id)
        if i-1 >= 0:
            size += add_to_bassin(j,i-1,id)
        if i+1 < len(heightmap[j]):
            size += add_to_bassin(j,i+1,id)
    return size

id = 0
bassin_size = []
for bassin_id in low_index:
    size = add_to_bassin(bassin_id[0], bassin_id[1], id)
    bassin_size.append(size)
    id = id +1

print(heightmap_bassin)



heightmap_bassin_size = [[-1] * len(lines[0].strip()) for j in range(len(lines))]
for j in range(len(heightmap_bassin)):
    for i in range(len(heightmap_bassin[j])):
        if heightmap_bassin[j][i] != -1:
            heightmap_bassin_size[j][i] = bassin_size[heightmap_bassin[j][i]]

print(heightmap_bassin_size)
with sns.axes_style("white"):
    f, ax = plt.subplots(figsize=(20, 10))
    ax = sns.heatmap(heightmap_bassin_size, cmap="magma")
    f.savefig("day9/heightmap_bassin.png")

bassin_size.sort(reverse=True)
print(bassin_size)
print(bassin_size[0]*bassin_size[1]*bassin_size[2])
input_loc = "day15/input.txt"

with open(input_loc) as f:
    lines = f.readlines()

risk_map = [[0] * len(lines[0].strip()) for i in range(len(lines))]
risk_map_dist = [[10000000000] * len(lines[0].strip()) for i in range(len(lines))]
visited = [[False] * len(lines[0].strip()) for i in range(len(lines))]

for j in range(len(lines)):
    l = lines[j]
    for i in range(len(l.strip())):
        risk_map[j][i] = int(l[i])

print(risk_map)
#print(risk_map_dist)

def add_cost_2( i, j, risk_map_dist, risk_map, current_cost, visited):
    if j >= 0 and j < len(risk_map_dist):
        if i >=0 and i < len(risk_map_dist[j]):
            cost2 = current_cost + risk_map[j][i]
            if risk_map_dist[j][i] > cost2:
                risk_map_dist[j][i] = cost2
                if visited[j][i]:
                    all_nodes.insert(0,[j,i])

def add_cost( current_pos, risk_map_dist, risk_map,visited):
    j = current_pos[0]
    i = current_pos[1]
    #print(risk_map_dist[j][i])
    current_cost = risk_map_dist[j][i]
    add_cost_2(i,j+1,risk_map_dist,risk_map,current_cost,visited)
    add_cost_2(i,j-1,risk_map_dist,risk_map,current_cost,visited)
    add_cost_2(i+1,j,risk_map_dist,risk_map,current_cost,visited)
    add_cost_2(i-1,j,risk_map_dist,risk_map,current_cost,visited)
    visited[j][i] = True
    #print(visited)

done = False
all_nodes = []
for j in range(len(risk_map)):
    for i in range(len(risk_map[j])):
        all_nodes.append([j,i])
risk_map_dist[0][0] = 0

while len(all_nodes) != 0:
    node = all_nodes.pop(0)
    add_cost(node,risk_map_dist,risk_map,visited)
    
#print(risk_map_dist)
print(risk_map_dist[-1][-1])

size = len(risk_map[0])
full_map = [[0]*size*5 for i in range(size*5)]
for j in range(len(risk_map)):
    for i in range(len(risk_map[j])):
        for j2 in range(0,5):
            for i2 in range(0,5):
                if j2 == 0 and i2 == 0:
                    full_map[j][i] = risk_map[j][i]
                else:
                    if j2 == 0:
                        full_map[j+j2*size][i+i2*size] = full_map[j][i+(i2-1)*size] + 1 if full_map[j][i+(i2-1)*size] < 9 else 1
                    elif i2 == 0:
                        full_map[j+j2*size][i+i2*size] = full_map[j+(j2-1)*size][i] + 1 if full_map[j+(j2-1)*size][i] < 9 else 1
                    else:
                        full_map[j+j2*size][i+i2*size] = full_map[j+(j2-1)*size][i+(i2)*size] + 1 if full_map[j+(j2-1)*size][i+(i2)*size] < 9 else 1

#risk_map = [[0] * len(lines[0].strip()) for i in range(len(lines))]
full_map_dist = [[10000000000] * len(full_map[0]) for i in range(len(full_map))]
full_visited = [[False] * len(full_map[0]) for i in range(len(full_map))]

all_nodes = []
for j in range(len(full_map)):
    for i in range(len(full_map[j])):
        all_nodes.append([j,i])
full_map_dist[0][0] = 0

while len(all_nodes) != 0:
    node = all_nodes.pop(0)
    add_cost(node,full_map_dist,full_map,full_visited)
print(full_map_dist[-1][-1])
print(full_map[-1])
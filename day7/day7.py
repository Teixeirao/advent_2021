
input_loc = "day7/input.txt"


with open(input_loc) as f:
    lines = f.readlines()

crab_initial_hor_pos = list(map(int, lines[0].split(",")))
data_size = max(crab_initial_hor_pos)

max_crab_pos = max(crab_initial_hor_pos)

done = False

crab_pos = crab_initial_hor_pos.copy()
fuel_per_pos = [[0] * len(crab_pos) for i in range(data_size)]
fuel_per_pos2 = [0] * data_size

for pos in range(0, data_size):
    for crab in range(0,len(crab_pos)):
        fuel_per_pos2[pos] += abs(crab_pos[crab]-pos)

print(fuel_per_pos2)
print(min(fuel_per_pos2))

fuel_per_pos3 = [0] * data_size
for pos in range(0, data_size):
    for crab in range(0,len(crab_pos)):
        move_by = abs(crab_pos[crab]-pos)
        # n(n+1)/2
        fuel_per_pos3[pos] += move_by * (move_by+1) / 2

print(min(fuel_per_pos3))
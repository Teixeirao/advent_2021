from collections import deque

input_loc = "day6/input.txt"

nb_day = 256

with open(input_loc) as f:
    lines = f.readlines()

# Slow version
lanternfish_state_init_state = list(map(int, lines[0].split(",")))
lanternfish_state = lanternfish_state_init_state.copy()
print(lanternfish_state)

if nb_day == 80:
    for day in range(0,nb_day):
        for fish_index in range(0,len(lanternfish_state)):
            if lanternfish_state[fish_index] == 0:
                lanternfish_state[fish_index] = 6
                lanternfish_state.append(8)
            else:
                lanternfish_state[fish_index] -= 1
        #print(lanternfish_state)

print(len(lanternfish_state))


# Fast version

# Count number of fish in a given state

lanternfish_count_by_age = deque([0]*9)
# initial setup
for fish_index in range(0,len(lanternfish_state_init_state)):
    lanternfish_count_by_age[lanternfish_state_init_state[fish_index]] += 1
print(lanternfish_count_by_age)

for day in range(0,nb_day):
    nb_zero = lanternfish_count_by_age[0]
    lanternfish_count_by_age.rotate(-1)
    lanternfish_count_by_age[6] += nb_zero
    lanternfish_count_by_age[8] =  nb_zero
    #print(lanternfish_count_by_age)

print("{0}".format( sum(lanternfish_count_by_age) ))
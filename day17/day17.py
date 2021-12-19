# Exemple target area: x=20..30, y=-10..-5
test_target_area = [[20,30],[-10,-5]]

# target area: x=70..96, y=-179..-124
real_target_area = [[70,96],[-179,-124]]

def simulate_probe(initial_x_v, initial_y_v, target):
    done = False
    x_v = initial_x_v
    y_v = initial_y_v
    x = 0
    y = 0
    max_y = y
    while not done:
        x += x_v
        y += y_v
        x_v += -1 if x_v > 0 else ( 1 if x_v < 0 else 0 )
        y_v -= 1
        max_y = max([y,max_y])
        if x in range(target[0][0],target[0][1]+1):
            if y in range(target[1][0],target[1][1]+1):
                return True, max_y
        if x > target[0][1]:
            return False,-1
        if ( x < target[0][0] ) and x_v == 0:
            return False, -1
        if y < target[1][0]:
            return False, -1

y_max = 0
target = real_target_area
all_valid = []
for initial_x in range(target[0][1]+1): # 
    for initial_y in range(target[1][0],1000): # ugly, there should be a way to calculate max initial_y based on initial_x
        good, c_max = simulate_probe(initial_x,initial_y, target)
        if good:
            all_valid.append([initial_x,initial_y])
        y_max = max(y_max,c_max)

print(y_max)
print(all_valid)
print(len(all_valid))
print(simulate_probe(23,-10,test_target_area))

#with open("day17/test.txt") as f:
#    lines = f.readlines()
#    la = lines[0].strip().split()
#    for cc in la:
#        x = int(cc.split(",")[0])
#        y = int(cc.split(",")[1])
#        if [x,y] not in all_valid:
#            print ( "missing {0},{1}".format(x,y))
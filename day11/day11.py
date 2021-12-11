input_loc = "day11/input.txt"

with open(input_loc) as f:
    lines = f.readlines()


init_octo_energy = [[-1] * (len(lines[0])-1+2) for i in range(len(lines)+2)]
for li in range(len(lines)):
    l = lines[li]
    for lc in range(len(l.strip())):
        init_octo_energy[li+1][lc+1] = int(l[lc])

print(init_octo_energy)

def flashes(octo_energy):
    nb_flash = 0
    for j in range(1,len(octo_energy)-1):
        for i in range(1,len(octo_energy[j])-1):
            if octo_energy[j][i] > 9:
                #print("ICI")
                nb_flash += 1
                octo_energy[j][i] = -1 
                octo_energy[j+1][i] += 1 if octo_energy[j+1][i] != -1 else 0
                octo_energy[j-1][i] += 1 if octo_energy[j-1][i] != -1 else 0
                octo_energy[j][i+1] += 1 if octo_energy[j][i+1] != -1 else 0
                octo_energy[j][i-1] += 1 if octo_energy[j][i-1] != -1 else 0
                octo_energy[j+1][i+1] += 1 if octo_energy[j+1][i+1] != -1 else 0
                octo_energy[j+1][i-1] += 1 if octo_energy[j+1][i-1] != -1 else 0
                octo_energy[j-1][i+1] += 1 if octo_energy[j-1][i+1] != -1 else 0
                octo_energy[j-1][i-1] += 1 if octo_energy[j-1][i-1] != -1 else 0
    if nb_flash != 0:
        nb_flash += flashes(octo_energy)
        #print(nb_flash)
    return nb_flash



def simulate_one_step(octo_energy):
    nb = 0
    for j in range(1,len(octo_energy)-1):
        for i in range(1,len(octo_energy[j])-1):
            octo_energy[j][i] += 1
    #print(octo_energy)
    
    nb = flashes(octo_energy)

    has_all_flashed = True
    for j in range(1,len(octo_energy)-1):
        for i in range(1,len(octo_energy[j])-1):
            if octo_energy[j][i] == -1:
                octo_energy[j][i] = 0
            else:
                has_all_flashed = False

    return [nb,has_all_flashed]

octo_energy = init_octo_energy.copy()
res = 0
cstep = 0
for i in range(100):
    r = simulate_one_step(octo_energy)
    res += r[0]
    #print(octo_energy)
    if r[1]:
        print("all flash {0}".format(r[1]))
    cstep += 1

done = False
while not done:
    r = simulate_one_step(octo_energy)
    res += r[0]
    cstep += 1
    #print(octo_energy)
    if r[1]:
        print("all flash {0} {1}".format(r[1],cstep))
        done = True


print(res)



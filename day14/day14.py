from collections import Counter

input_loc = "day14/input.txt"

with open(input_loc) as f:
    lines = f.readlines()


template = lines[0].strip()
insertion_map = dict()
for i in range(2,len(lines)):
    la = lines[i].split()
    insertion_map[la[0]] = la[2]


print(insertion_map)

nb_steps = 10
polymere = template
for i in range(nb_steps):
    polymere_temp = ""
    for j in range(len(polymere)):
        if j+1 < len(polymere):
            pair = polymere[j:j+2]
            #print(pair)
            polymere_temp += pair[0] + insertion_map[pair]
        else:
            polymere_temp += polymere[j]

    polymere = polymere_temp

poly_count = Counter(polymere)
max_c = max(poly_count.values())
#max_c =  list(poly_count.values()).index(max_c_s)

#print(list(poly_count.values()))
min_c = min(poly_count.values())
#min_c = list(poly_count.values()).index(max_c_s)

print(max_c-min_c)

#print(polymere)

nb_steps = 40
polymere = template

pairs = dict()
count = dict()
remainder = ""
for j in range(len(polymere)):
    if j+1 < len(polymere):
        if polymere[j:j+2] in pairs:
            pairs[polymere[j:j+2]] += 1
        else:
            pairs[polymere[j:j+2]] = 1
    l = polymere[j]
    if l in count:
        count[l] += 1
    else:
        count[l] = 1

for i in range(nb_steps):
    pairs_tmp = dict()
    for p in pairs:
        match = insertion_map[p]
        p0 = p[0] + match
        p1 = match + p[1]
        if p0 in pairs_tmp:
            pairs_tmp[p0] += pairs[p]
        else:
            pairs_tmp[p0] = pairs[p]
        if p1 in pairs_tmp:
            pairs_tmp[p1] += pairs[p]
        else:
            pairs_tmp[p1] = pairs[p]
        if match in count:
            count[match] += pairs[p]
        else:
            count[match] = pairs[p]
    print(pairs_tmp)
    pairs = pairs_tmp

print(count)

max_key = max(count, key=count.get)
min_key = min(count, key=count.get)
print(max_key)
print(min_key)
print(count[max_key]-count[min_key])
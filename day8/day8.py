


input_loc = "day8/input_ex_2.txt"
digit_map = {
    0 : ["a","b","c","e","f","g"],
    1 : ["c","f"],
    2 : ["a","c","d","e","g"],
    3 : ["a","c","d","f","g"],
    4 : ["b","c","d","f"],
    5 : ["a","b","d","f","g"],
    6 : ["a","b","d","e","f","g"],
    7 : ["a","c","f"],
    8 : ["a","b","c","d","e","f","g"],
    9 : ["a","b","c","d","f","g"]
}

digi_map_2 = dict()
digi_map_3 = dict()
digi_map_strk = dict()
for nb in digit_map:
    digi_map_2[nb] = {
        "map" : digit_map[nb],
        "stroke" : len(digit_map[nb])
    }
    digi_map_3[digit_map[nb]] = nb



print(digi_map_2)

with open(input_loc) as f:
    lines = f.readlines()


nb = 0
for l in lines:
    la = l.split("|")[1].split()
    for strk in la:
        #print(strk)
        #print(len(strk))
        if ( len(strk) == 2 ) or ( len(strk) == 4 ) or ( len(strk) == 3 ) or ( len(strk) == 7 ):
            nb += 1


print(nb)

def add_to_potential_map(potential_maps, expected, real, number):
     potential_maps[number][real].add(expected)

def get_potential_map_excluded(potential_maps):
    reduced_map = {}
    for letter in ["a","b","c","d","e","f","g"]:
        s = set()
        print(letter)
        for nb in [2,4,3,7,6,5]:
            if len(s) == 0 :
                if len(potential_maps[nb][letter]) != 0:
                    s = potential_maps[nb][letter]
            elif len(potential_maps[nb][letter]) != 0:
                s = s.intersection(potential_maps[nb][letter])
                if letter == "g":
                    print(nb)
                    print(potential_maps[nb][letter])
                    print(s)
               
        reduced_map[letter] = s

    done = False
    cnt_done = 0
    while not done:
        print(reduced_map)
        for letter in ["a","b","c","d","e","f","g"]:
            cnt = 1
            for letter2 in ["a","b","c","d","e","f","g"]:
                if letter != letter2:
                    if reduced_map[letter] == reduced_map[letter2]:
                        cnt += 1
            if cnt == len(reduced_map[letter]) or len(reduced_map[letter]) == 1 :
                for letter2 in ["a","b","c","d","e","f","g"]:
                    if letter != letter2:
                        if reduced_map[letter] != reduced_map[letter2]:
                            reduced_map[letter2] = reduced_map[letter2] - reduced_map[letter]
            if len(reduced_map[letter]) == 1:
                cnt_done += 1
        if cnt_done == 8:
            done = True

        

    print("reduced")
    print(reduced_map)
    return reduced_map




strk_map = {
    2: [1],
    4: [4],
    3: [7],
    7: [8],
    6: [0,6,9],
    5: [2,3,5]
}
strk_map2 = {
    2: ["c","f"],
    4: ["b","c","d","f"],
    3: ["a","c","f"],
    7: ["a","b","c","d","e","f","g"],
    6: ["a","b","c","e","f","g","d"],
    5: ["a","c","d","e","g","f","b"]
}
for l in lines:
    la = l.split("|")[0].split() + l.split("|")[1].split()
    potential_maps = [{"a" : set(), "b": set(), "c": set(), "d":set(), "e": set(), "f":set(), "g":set()} for i in range(10)]
    #print(la)
    for strk in la:
        #for number in strk_map[len(strk)]:
        for expected in strk_map2[len(strk)]:
            for i in range(len(strk)):
                add_to_potential_map(potential_maps, expected, strk[i], len(strk))
    print(potential_maps)
    rmap = get_potential_map_excluded(potential_maps)
    #map_4_digit(rmap,l.split("|")[1])
        
        
        #or ( len(strk) == 4 ) or ( len(strk) == 3 ) or ( len(strk) == 7 ):
        #    nb += 1
        


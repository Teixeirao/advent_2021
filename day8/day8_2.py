from itertools import permutations

input_loc = "day8/input.txt"
abcdefg = ["a","b","c","d","e","f","g"]
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

with open(input_loc) as f:
    lines = f.readlines()

strk_map = {
    2: [1],
    4: [4],
    3: [7],
    7: [8],
    6: [0,6,9],
    5: [2,3,5]
}

strk_map2 = {
    2: [set(["c","f"]), set(["a","b","d","e","g"])],
    4: [set(["b","c","d","f"]), set(["a","e","g"])],
    3: [set(["a","c","f"] ), set(["b","d","e","g"])], 
    7: [set(["a","b","c","d","e","f","g"]), set()],
    6: [set(["a","b","c","d","e","f","g"]), set()],
    5: [set(["a","b","c","d","e","f","g"]), set()],
}

strk_map3 = {
    2: [["c","f"], set(["a","b","d","e","g"])],
    4: [["b","c","d","f"], set(["a","e","g"])],
    3: [["a","c","f"], set(["b","d","e","g"])], 
    7: [["a","b","c","d","e","f","g"], set()],
    6: [["a","b","c","d","e","f","g"], set()],
    5: [["a","b","c","d","e","f","g"], set()],
}

def is_valid(current_map, list_of_strk):
    find_cnt = 0
    all_numbers = []
    print(current_map)
    for strk in list_of_strk:
        segment = []
        for i in range(len(strk)):
            index = current_map.index(strk[i])
            segment.append(abcdefg[index])
        segment.sort()
        for pot in strk_map[len(strk)]:
            
            if digit_map[pot] == segment:
                print("strk: {0}, pot: {1}, segment: {2}".format(strk, pot, segment))
                find_cnt += 1
                all_numbers.append(pot)

    print(find_cnt)
    return [find_cnt == len(list_of_strk), all_numbers[-4:]]
   




def create_map(index,map,current_map, list_of_strk):
    if index == 7:
        if len(set(current_map) & set(abcdefg)) == 7:
           return [is_valid(current_map, list_of_strk), current_map]
        else:
            return [[False,[]], current_map]
   
    for mapl in map[abcdefg[index]]:
        if index == 0:
            current_map = []
        current_map.append(mapl)
        #print(index)
        #print(mapl)
        #print(current_map)
#
        rset = create_map(index+1,map,current_map, list_of_strk)
        if rset[0][0]:
            return rset
        else:
            current_map.pop(-1)
    return [[False,[]],[]]


res_sum = 0
for l in lines:
    la = l.split("|")[0].split() + l.split("|")[1].split()
    pmap = { a : set(["a","b","c","d","e","f","g"]) for a in abcdefg }
    #pmap = { a : set() for a in abcdefg }
    for strk in la:
        nb = len(strk)
        if nb == 2 or nb == 4 or nb == 3:
            nset = set()
            for i in range(len(strk)):
                nset.add(strk[i])
             
            for j in strk_map3[nb][0]:
                pmap[j] &= nset
                #pmap[strk[i]] = ( pmap[strk[i]] - strk_map2[nb][1] ) & strk_map2[nb][0]
            print(pmap)
    res = create_map(0, pmap, [], la)
    res_sum += int("{0}{1}{2}{3}".format(res[0][1][0], res[0][1][1], res[0][1][2], res[0][1][3]))
    print( res )
print(res_sum)

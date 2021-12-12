class Cave:

    def __init__(self, name):
        self.name = name
        self.connections = []
        self.isSmall = name.islower()
        self.isend = (name == "end")
        self.visited = 0

    def add_connection(self, connecting_cave):
        self.connections.append( connecting_cave )

    #def set_isend(self):
    #    self.isend = True
 
    def visit_count(self):
        return self.visited

    def get_connections(self):
        return self.connections

    def print(self):
        print( "{0} {1} {2} {3} {4} ".format(self.name, self.connections, self.isSmall, self.isend, self.visited))
    
def search_path_dfs(c, small_visit_list, pstring):
    nb_path = 0
    #print(c.name)

    if c.isend:
        #print(pstring)
        return 1

    for connect in c.get_connections():
        if connect.name != "start":
            #if ( connect not in small_visit_list ): #v1
            if ( connect not in small_visit_list ):
                #print(small_visit_list)
                if connect.isSmall:
                    small_visit_list2 = small_visit_list.copy()
                    small_visit_list2.append(connect)
                    nb_path += search_path_dfs(connect, small_visit_list2, pstring + "->" + connect.name)
                else:
                    nb_path += search_path_dfs(connect, small_visit_list.copy(), pstring + "->" + connect.name)
            else: #v2
                #print("LA")
                #print(small_visit_list)
                mxsmall = max(small_visit_list,key=small_visit_list.count)
                if small_visit_list.count(mxsmall) < 2:
                    #print("ICI")
                    small_visit_list2 = small_visit_list.copy()
                    small_visit_list2.append(connect)
                    nb_path += search_path_dfs(connect, small_visit_list2, pstring + "->" + connect.name)


    return nb_path


input_loc = "day12/input.txt"

with open(input_loc) as f:
    lines = f.readlines()

all_caves = dict()
starting_caves = []
for l in lines:
    #if "start" in l:
    #    n = l.strip().split("-")[0]
    #    if "start-" in l:
    #        n = l.strip().split("-")[1]
    #    c = Cave(n)
    #    all_caves[n] = c
    #    starting_caves.append(c)
    #elif "end" in l:
    #    n = l.strip().split("-")[0]
    #    if "end-" in l:
    #        n = l.strip().split("-")[1]
#
    #    if n not in all_caves:
    #        c = Cave(n)
    #        all_caves[n] = c
    #        c.set_isend()
    #    else:
    #        all_caves[n].set_isend()
    #        
    #else:
    n0 = l.strip().split("-")[0]
    n1 = l.strip().split("-")[1]
    c0 = None
    c1 = None
    if n0 not in all_caves:
        c0 = Cave(n0)
        all_caves[n0] = c0
        if n0 == "start":
            starting_caves.append(c0)
    else:
        c0 = all_caves[n0]
    
    if n1 not in all_caves:
        c1 = Cave(n1)
        all_caves[n1] = c1
        if n1 == "start":
            starting_caves.append(c1)
    else:
        c1 = all_caves[n1]

    c0.add_connection(c1)
    c1.add_connection(c0)




for n in all_caves:
    all_caves[n].visited = 0
    all_caves[n].print()

#print(starting_caves)
total = 0
for scave in starting_caves:
    for n in all_caves:
        all_caves[n].visited = 0
        #all_caves[n].print()
    small_visited = []
    #if scave.isSmall:
    #    small_visited.append(scave)
    n = search_path_dfs(scave, small_visited, scave.name)
    total += n
    #print(n)

print(total)


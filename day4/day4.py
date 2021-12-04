class board:
    def __init__(self):
        self.board = [[False,False,False,False,False],
                      [False,False,False,False,False],
                      [False,False,False,False,False],
                      [False,False,False,False,False],
                      [False,False,False,False,False]]
        self.board_loc = dict()


    def create_board(self, lines):
        r = 0
        for l in lines:
            c = 0
            for n in l.split():
                self.board_loc[n] = [r,c]
                c += 1
            r += 1

    def reset_board(self):
        self.board = [[False,False,False,False,False],
                      [False,False,False,False,False],
                      [False,False,False,False,False],
                      [False,False,False,False,False],
                      [False,False,False,False,False]]

    def add_drawn_nb(self, nb):
        if nb in self.board_loc:
            #print("ICI")
            self.board[self.board_loc[nb][0]][self.board_loc[nb][1]] = True

    def check_board(self):
        for r in range(0,5):
            valid = True
            for c in range(0,5):
                valid = valid and self.board[r][c]
            if valid:
                return True
        
        for c in range(0,5):
            valid = True
            for r in range(0,5):
                valid = valid and self.board[r][c]
            if valid:
                return True

        return False

    def get_unmarked_sum(self):
        sum = 0
        for nb in self.board_loc:
            if not (self.board[self.board_loc[nb][0]][self.board_loc[nb][1]]):
                sum += int(nb)
        return sum

    def print(self):
        print(self.board)
        print(self.board_loc)


with open("day4/input.txt") as f:
    lines = f.readlines()

draws = lines[0]

cnt = 2
all_boards = []

while cnt < len(lines):
    b = board()
    b.create_board(lines[cnt:cnt+5])
    all_boards.append(b)
    cnt += 6

#for b in all_boards:
#    b.print()

wining_board = None
wining_nb = -1
done = False
for nb in draws.split(","):
    #print(nb)
    if done:
        break
    for b in all_boards:
        b.add_drawn_nb(nb)
        #b.print()
        if b.check_board():
            wining_board = b
            wining_nb = int(nb)
            done = True
        if done:
            break

wining_board.print()

#print(wining_board.get_unmarked_sum())
print("pb1 {0}".format(wining_board.get_unmarked_sum()*wining_nb))


last_wining_board = None
last_wining_nb = -1
non_wining_boards = all_boards.copy()

for b in non_wining_boards:
    b.reset_board()

for nb in draws.split(","):
    for b in list(non_wining_boards):
        b.add_drawn_nb(nb)
        if b.check_board():
            last_wining_board = b
            last_wining_nb = int(nb)
            non_wining_boards.remove(b)


last_wining_board.print()
print("pb2 {0}".format(last_wining_board.get_unmarked_sum()*last_wining_nb))

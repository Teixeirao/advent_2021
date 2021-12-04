

prev = -1
cnt = 0
cnt2 = 0
window = [-1,-1,-1,-1]
with open("day1/input.txt") as f:
    lines = f.readlines()
    for l in lines:
        depth = int(l)
        window[0] = window[3]
        window[3] = window[2] + depth if window[2] != -1 else -1
        window[2] = window[1] + depth if window[1] != -1 else -1
        window[1] = depth
        
        print(window)

        if window[0] != -1 and window[0] < window[3]:
            cnt2 += 1

        if prev != -1 and depth > prev:
            cnt += 1
        prev = depth

print("pb1 {0}".format(cnt))
print("pb2 {0}".format(cnt2))





from collections import deque

q = int(input())
d = deque([])

for _ in range(q):
    t, x = input().split()
    x = int(x)
    if t == "1":
        d.appendleft(x)
    elif t == "2":
        d.append(x)
    else:
        print(d[x - 1])
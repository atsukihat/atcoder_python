# 2重配列にして、グラフの隣接リストを作る

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

res = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

for i in range(n):
    cnt = 0
    for num in graph[i]:
        if i > num:
            cnt += 1
    if cnt == 1:
        res += 1

print(res)
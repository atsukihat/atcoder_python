h, w = map(int, input().split())
A = [[int(x) for x in input().split()] for i in range(h)]

row = [sum(a) for a in A]
col = [0 for _ in range(w)]

# for i in range(h):
#     for j in range(w):
#         row[i] += A[i][j]

for j in range(w):
    for i in range(h):
        col[j] += A[i][j]


# 初期化
result = [[0]*w for _ in range(h)]

for i in range(h):
    for j in range(w):
        result[i][j] = row[i] + col[j] - A[i][j]

for r in result:
    print(*r)

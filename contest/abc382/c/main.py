# 定数の定義
K = 200010

# 入力の受け取り
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# id配列を初期化（-1で埋める）
id = [-1] * K
r = K

# id配列を構築
for i in range(n):
    a = A[i]
    while r > a:
        r -= 1
        id[r] = i + 1  # 人の番号は1始まり

# クエリの処理
for b in B:
    print(id[b])

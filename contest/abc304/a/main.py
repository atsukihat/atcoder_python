# 入力
N = int(input())
# 年齢を保存するリスト
age = []
# 名前を保存するリスト
name = []

for i in range(N):
    # 入力
    S, A = input().split()
    # Aだけ整数型
    A = int(A)
    age.append(A)
    name.append(S)
# 最年少の場所をインデックスで保存
min_age_index = age.index(min(age))
for i in range(N):
    # 時計回りに出力
    print(name[(min_age_index+i) % N])
    # Nで割ったあまりにすることで、indexの調整

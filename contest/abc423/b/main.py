# 左右から、順にリストを確認して、配列の値が1であればそこまでの距離を記録する
# 例外：もし、全てが0であれば（1が１つもない）、全ての部屋を訪れることができるので、0を出力する
# 例外：部屋が2個しかない場合はLが1のみであっても全ての部屋を訪れることができる。

n = int(input())
keys = list(map(int, input().split()))

# 訪れることが可能な部屋の数
ava = 2

for key in keys:
    if key == 0:
        ava += 1
    elif key == 1:
        break

for key in reversed(keys):
    if key == 0:
        ava += 1
    elif key == 1:
        break

ans = n + 1 - ava

if keys.count(1) == 0 or keys.count(1) == 1:
    ans = 0

print(ans)
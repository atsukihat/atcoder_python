# 実装が２重ループになってしまったため、計算量がO(n^2)になってしまっている。

n = int(input())
LowCoder = set()

for i in range(n):
    s = input()
    if s not in LowCoder:
        LowCoder.add(s)
        print(i+1)
    else:
        continue
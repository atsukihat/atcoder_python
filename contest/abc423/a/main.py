# 1000円単位で、手数料込みでどのくらい引き出せるかを計算する
# 引き出し可能額を仮置きして、手数料と合算した値とを求める
# そもそも 1 <= x < 1000 の場合は 0 を出力する
# 引き出し額が 1000 に満たない場合も 0 を出力する
# 例外：

x, c = map(int, input().split())

ans = x // 1000 * 1000

while True:
    charge = ans // 1000 * c
    if x < ans + charge:
        ans -= 1000
    elif ans < 1000:
        ans = 0
        break
    else:
        break


print(ans)

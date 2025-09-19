# 3つの変数の最大公約数を求めて、その値でそれぞれの変数を割った値から1を引いた値を合計する
import math

a, b, c = map(int, input().split())
g = math.gcd(math.gcd(a, b), c)

ans = (a // g - 1) + (b // g - 1) + (c // g - 1)
print(ans)
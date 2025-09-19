# 8進数を9進数に変換する
# 9進数の5を8に変換する

n, k = input().split()
k = int(k)


def base8_to_base10(n: str) -> int:
    return int(n, 8)


def base10_to_base9(n: int) -> str:
    if n == 0:
        return "0"
    res = ""
    while n > 0:
        res = str(n % 9) + res
        n //= 9
    return res


def base9_to_base8(n: str) -> str:
    res = ""
    for c in n:
        if c == "8":
            res += "5"
        else:
            res += c
    return res


for _ in range(k):
    n = base10_to_base9(base8_to_base10(n))
    n = base9_to_base8(n)

print(n)
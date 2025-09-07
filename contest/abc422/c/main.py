n = int(input())

# 作成可能はコンテストのパターンは3通り
#  aac, abc, acc の3パターン
# a > c の場合は b > c であれば 最大で c 個のコンテストが作成可能
# a > c の場合は b < c であれば ((a-c)+b) > c であれば 最大で c 個のコンテストが作成可能
# a > c の場合は b < c であれば ((a-c)+b) < c であれば 最大で ((a-c)+b) 個のコンテストが作成可能
# a == c の場合は b > c であれば最大で c 個のコンテストが作成可能
# a < c の場合は b > a であれば 最大で a 個のコンテストが作成可能


for _ in range(n):
    a, b, c = map(int, input().split())
    if a > c:
        if b >= c:
            print(c)
        else:
            if (a - c) + b >= c:
                print(c)
            else:
                print((a - c) + b + c)
    elif a == c:
        if b >= c:
            print(c)
        else:
            print(b)
    else:  # a < c
        if b >= a:
            print(a)
        else:
            if (c - a) + b >= a:
                print(a)
            else:
                print((c - a) + b + a)

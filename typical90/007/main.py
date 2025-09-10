n = int(input())
a = list(map(int, input().split()))
q = int(input())
a.sort()

for _ in range(q):
    b = int(input())

    # aの中でbに最も近い値を二分探索で探す
    left = 0
    right = n-1
    while abs(left - right) > 1:
        mid = (left + right) // 2
        if a[mid] < b:
            left = mid
        else:
            right = mid

    if abs(a[left] - b) <= abs(a[right] - b):
        print(abs(a[left] - b))
    else:
        print(abs(a[right] - b))

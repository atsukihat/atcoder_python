n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0

for i in range(n):
    count += abs(a[i] - b[i])


if count > k or (count - k) % 2 != 0:
    print("No")
else:
    print("Yes")
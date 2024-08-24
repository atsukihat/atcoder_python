from collections import deque

N = int(input())
H = deque(map(int, input().split()))

T = 0

while H:
    current = H[0]

    if current >= 5:
        quotient = current // 5
        remainder = current % 5

        T += 3 * quotient

        H[0] = remainder

    if H[0] <= 0:
        H.popleft()
    else:
        T += 1

        if T % 3 == 0:
            H[0] -= 3
        else:
            H[0] -= 1

        if H[0] <= 0:
            H.popleft()

print(T)

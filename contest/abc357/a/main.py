N, M = map(int, input().split())
H = list(map(int, input().split()))

rest = M
result = 0

for hands in H:
    if rest - hands < 0:
        break
    else:
        result += 1
        rest -= hands
        
print(result)
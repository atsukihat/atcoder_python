n, d = map(int, input().split())
s = input().strip()

ans = []

for i in reversed(range(n)):
    if s[i] == '@':
        if d > 0:
            d -= 1
            ans.append(".")
        else:
            ans.append("@")
    else:
        ans.append(s[i])

for i in reversed(range(n)):
    print(ans[i], end="")

print()

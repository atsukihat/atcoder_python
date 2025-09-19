n = int(input())
st = [list(map(int, input().split())) for _ in range(n)]

# 1組と2組で別々に累積和を求める。

cumsum1 = [0] * (n+1)
cumsum2 = [0] * (n+1)

for i in range(n):
    cumsum1[i + 1] = cumsum1[i] + (st[i][1] if st[i][0] == 1 else 0)
    cumsum2[i + 1] = cumsum2[i] + (st[i][1] if st[i][0] == 2 else 0)

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())

    ans_st1 = cumsum1[r] - cumsum1[l - 1]
    ans_st2 = cumsum2[r] - cumsum2[l - 1]
    print(ans_st1, ans_st2)
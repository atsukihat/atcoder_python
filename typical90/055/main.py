# もし最初にstartがend以上だった場合、そのループは1回も実行されずにスキップされる
# atcoderは2秒以上かかるとTLEになる。目安は1秒間に10^8回(1億)の計算

n, p, q = map(int, input().split())
a = list(map(int, input().split()))

ans = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            for l in range(k+1, n):
                for m in range(l+1, n):
                    if (a[i] % p) * (a[j] % p) * (a[k] % p) * (a[l] % p) * (a[m] % p) % p == q:
                        ans += 1

print(ans)
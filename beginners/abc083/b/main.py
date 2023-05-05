n, a, b = map(int, input().split())
total = 0
for i in range(1, n+1):
    if (a <= sum(map(int, str(i))) <= b):
        total += i
print(total)

# N, A, B = map(int, input().split())
# print(sum(i for i in range(1, N+1) if A <= sum(map(int, str(i))) <= B))
# 不要な変数を省いた式

# n,a,b = list(map(int,input().split()))
# count=0
# for i in range(1,n+1):
#   x=str(i)
#   sum=0
#   for j in x: # 文字列の各行を参照する
#     sum+=int(j)
#   if a<=sum and sum<=b:
#     count+=i
# print(count)

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# A,B のすべての要素は互いに相異なります。

C = A + B

C_sorted = sorted(C)

res_string = "No"

for i in range(N+M-1):
    if (C_sorted[i] in A) & (C_sorted[i+1] in A):
        res_string = "Yes"
        break
          
if res_string == "Yes":
    print("Yes")
else:
    print("No")
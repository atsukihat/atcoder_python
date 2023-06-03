N = int(input())
A = list(map(int, input().split()))

for i in (len(A)):
    if ((A[i]-A[i+1] == abs(1))):
        i = i+1
    else:
        for m in len(abs([A[i]-A[i+1]-1])):
            if (A[i] > A[i+1]):
                

N = (int, input().split())
A = list(map(int, input().split()))


# 配列の中で正の数を数える
def count_positive_elements(arr):
    return sum(1 for x in arr if x > 0)


count = 0


# 降順に並び替える
while count_positive_elements(A) > 1:
    A.sort(reverse=True)
    A[0] -= 1
    A[1] -= 1
    count += 1
    
    # print(count_positive_elements(A))
    # print(A)
    # print(count)
    # print('---')

print(count)

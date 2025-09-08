n, l = map(int, input().split())
k = int(input())
a = list(map(int, input().split()))

yokan = []
part = 0

for sep in a:
    yokan.append(sep - part)
    part = sep

yokan.append(l - part)


def is_ok(x):
    count = 0
    length = 0

    for i in yokan:
        length += i
        if length >= x:
            count += 1
            length = 0

    return count >= k + 1


# 2分探索技でスコアが最も高くなるxを求める
def binary_search():
    left = 0
    right = l + 1

    while right - left > 1:
        mid = (left + right) // 2

        if is_ok(mid):
            left = mid
        else:
            right = mid

    return left


result = binary_search()
print(result)
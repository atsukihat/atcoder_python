N = int(input())
a = sorted(map(int, input().split()))[::-1]
print(sum(a[::2])-sum(a[1::2]))

# Pythonのスライス表記[::]は、リストや文字列の一部分を取り出すことができる機能
# [開始位置:終了位置:ステップ数]
# [::]を指定すると、開始位置と終了位置は省略され、リストや文字列全体が選択されます。ステップ数が負の場合、逆順に取り出されます。

# n = int(input())
# a = list(map(int, input().split()))
# la=[]
# lb=[]
# a.sort(reverse=True)
# for i in range(n):
#   if i==0 or i%2==0:
#     la.append(a[i])
#   else:
#     lb.append(a[i])
# pa=sum(la)
# pb=sum(lb)
# print(pa-pb)

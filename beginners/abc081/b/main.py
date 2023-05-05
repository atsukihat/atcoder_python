N = int(input())  # input関数はstring型で受け取るのでint型に変更
A = list(map(int, input().split()))  # 全てを一気に読み込む必要があるのでlist型を用いる
count = 0
while all(a % 2 == 0 for a in A):  # all() は、引数に与えられた要素がすべて True の場合に True を返し、それ以外の場合には False を返す組み込み関数
    A = [a/2 for a in A]    # Pythonのリスト内包表記 [式 for 変数 in イテラブルオブジェクト]
    count += 1
print(count)


# n=int(input())
# a = list(map(int,input().split()))
# count=0
# count2=0
# ok=True
# while ok==True:
#   for i in a:
#     if i%2==0:
#       if count==n:
#         a = [s/2 for s in a]
#         count=0 #配列の何個目かカウントする変数
#         count2+=1 #全て偶数であった回数をカウントする変数。
#         break
#       count+=1
#       continue
#     else:
#       ok=False
#       break
# print(count2)

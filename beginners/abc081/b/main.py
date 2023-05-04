N = int(input())  # input関数はstring型で受け取るのでint型に変更
A = list(map(int, input().split()))  # 全てを一気に読み込む必要があるのでlist型を用いる
count = 0
while all(a % 2 == 0 for a in A):  # all() は、引数に与えられた要素がすべて True の場合に True を返し、それ以外の場合には False を返す組み込み関数
    A = [a/2 for a in A]    # Pythonのリスト内包表記 [式 for 変数 in イテラブルオブジェクト]
    count += 1
print(count)

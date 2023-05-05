N = int(input())
d = [input() for i in range(N)]
print(len(set(d)))

# リスト内包表記の別事例
# d = []
# for i in range(N):
#     x = input()
#     d.append(x)

# このコードでは、入力された文字列のリスト d の要素数を求めています。
# len() はリストの要素数を取得するための関数で、set() は集合（重複を許さない要素の集まり）を作成するための組み込み関数です。

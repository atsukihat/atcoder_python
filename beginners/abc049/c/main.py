import re
S = input()
print("YES" if re.match("^(dream|dreamer|erase|eraser)+$", S) else "NO")

# re.match() は、指定された正規表現が文字列の先頭でマッチする場合にマッチオブジェクトを返します。マッチしない場合は None を返します。
# `^` は正規表現パターンの先頭を表します。例えば `^a` は、文字列の先頭が "a" である場合にマッチします。
# `$` は正規表現パターンの末尾を表します。例えば `a$` は、文字列の末尾が "a" である場合にマッチします。
# `^` と `$` を組み合わせて使うと、正規表現が文字列全体に一致するように制限できます。つまり、`^` と `$` で囲まれた部分は文字列全体を表し、その部分にマッチする正規表現パターンにだけマッチします。
# 例えば、`^(dream|dreamer|erase|eraser)+$` は、"dream"、"dreamer"、"erase"、"eraser" からなる文字列にのみマッチする正規表現パターンです。`+` は、直前の表現が 1 回以上繰り返されることを表します。


# 一般的な解答
# s = input()
# while s:
#   for query in ("erase", "eraser", "dream", "dreamer"):
#     if s.endswith(query):
#       s = s[:-len(query)] #s[0:-len(query):1]と同義。すなわち、query分を末尾から削除したsに更新する。
#       break #それを囲んでいる最も内側のループ（for文や次回取り上げるwhile文）を終了させる。
#   else: # breakされなかったとき、つまり、"erase", "eraser", "dream", "dreamer"どれも合致しなかった場合。elseを配置する場所(インデント回数)に注意。
#     print('NO')
#     exit() #プログラム終了
# print('YES')

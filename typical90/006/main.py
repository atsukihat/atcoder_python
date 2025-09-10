n, k = map(int, input().split())
s = input()


# この文字列sの中で最小の文字を選ぶ。最小の文字列以降で最小の文字を選ぶ。これをk回繰り返す
# ただし、残りの文字列の長さがk未満になった場合は、選択した最小の文字列よりも手前の文字列から最小の文字を選ぶ。
# kが0になるまで繰り返す。

def select_min_dic(k, s):

    res = []
    current_index = 0

    for i in range(k):

        # 選択した最小の文字以降の文字数がk-i未満の場合を考慮
        remaining_count = k - i

        # そもそも文字列のremaining_count分だけ省いたところから最小の文字を選ぶ
        search_end_index = len(s) - remaining_count + 1

        search_slice = s[current_index:search_end_index]

        min_char = min(search_slice)
        res.append(min_char)
        current_index = s.index(min_char, current_index) + 1

    return res


ans = select_min_dic(k, s)
print(''.join(ans))


# # res[i][c] := i 文字目以降で最初に文字 c が登場する index
# # 存在しないときは N
# def calc_next(S):
#     # 文字列 S の長さ
#     N = len(S)

#     # 答え
#     res = [[N] * 26 for _ in range(N + 1)]

#     # 後ろから見る
#     for i in range(N - 1, -1, -1):
#         # i + 1 文字目以降の結果を一旦 i 文字にコピー
#         for j in range(26):
#             res[i][j] = res[i + 1][j]

#         # i 文字目の情報を反映させる
#         res[i][ord(S[i]) - ord('a')] = i

#     # 答えを返す
#     return res


# # 入力
# N, K = map(int, input().split())
# S = input()

# # 前処理
# res = ''
# nex = calc_next(S)

# # 貪欲法
# j = -1
# for i in range(K):
#     for ordc in range(26):
#         k = nex[j + 1][ordc]

#         # ちゃんと K 文字が作れれば OK
#         if N - k >= K - i:
#             res += chr(ord('a') + ordc)
#             j = k
#             break
# print(res)

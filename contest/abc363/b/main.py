# この問題は計算量に注意する必要がある
# 英小文字のみからなる長さNの文字列S
# 文字列Sの並び替えで得られる文字列の数は、S!/A!B!C!...で求められる。A、B、CはそれぞれSの中のa、b、cの数

from collections import Counter
from math import factorial

N, K = map(int, input().split())
S = input() 

# 文字列SからK個の文字列を抽出して、回文になる文字列を全て見つける。
# その際にKが偶数なら同じ文字が奇数個になるパターンを考えない。Kが奇数なら同じ文字が偶数個の文字列が偶数個、同じ文字が奇数個の文字列が奇数個になる場合のみ考える。
# 文字列Sにおいて、文字列の長さKを一つのまとまりと見て、並び替えの階上の計算を行う。


# 回文かどうかを確認するための関数
def is_palindrome(short_string):
    return short_string == short_string[::-1]
  

# 文字列Sから長さKの回文になる全ての文字列を見つける
def palindrome_substrings(S, K):
    unique_palindromes = set()
    for i in range(len(S) - K + 1):
        short_string = S[i:i + K]
        if is_palindrome(short_string):
            unique_palindromes.add(short_string)
    return unique_palindromes
  
# def palindrome_substrings(S, K):
#     unique_palindromes = set()
#     for i in range(len(S) - K + 1):
#         short_string = S[i:i + K]
#         if is_palindrome(short_string):
#             freq = Counter(short_string)
            
#             if K % 2 == 0:
#                 # Kが偶数の場合、全ての文字が偶数個になる
#                 if all(v % 2 == 0 for v in freq.values()):
#                     unique_palindromes.add(short_string)
#             else:
#                 # Kが奇数の場合、1つの文字が奇数個で、残りが全て偶数個になる
#                 odd_counts = sum(1 for v in freq.values() if v % 2 != 0)
#                 if odd_counts == 1:
#                     unique_palindromes.add(short_string)
#     return unique_palindromes


# 与えられた文字列の並び替えを計算する関数
def count_permutations(S):
    freq = Counter(S)
    denom = 1
    for count in freq.values():
        denom *= factorial(count)
    return factorial(len(S)) // denom
  
  
# 与えられた文字列の並び替えの総数を計算する
# 文字列Sから回文になる文字列を抽出して、その文字列の並び替えの総数を計算し、差分を計算する
def main(S, N, K):
    # 長さKの回文の部分文字列のセットを取得
    palindromes = palindrome_substrings(S, K)
    
    # S内の全ての並び替えの総数を計算
    total_permutations = count_permutations(S)
    
    # セットの回文部分文字列に基づいた並び替えの総数の合計を計算
    palindrome_permutations = 0
    for palindrome in palindromes:
        palindrome_permutations += count_permutations(palindrome)

    # 差分を計算
    result = total_permutations - palindrome_permutations
    
    # 結果を出力
    print(result)


# メイン関数の呼び出し
main(S, N, K)
from itertools import permutations


def main():
    n, k = map(int, input().split())
    s = input() 

    # 文字を対応する数値 (a = 0, b = 1, ...) に変換
    a = [(ord(char) - ord('a')) for char in s]
    
    # 順列を生成し、カウントを保持
    ans = 0
    
    # 全ての順列をチェック
    for perm in permutations(a):
        ok = True
        # 部分列毎に回文かどうかをチェック
        for i in range(n - k + 1):
            if list(perm[i:i+k]) == list(perm[i:i+k])[::-1]:
                ok = False
                break
        if ok:
            ans += 1
    
    print(ans)

if __name__ == '__main__':
    main()
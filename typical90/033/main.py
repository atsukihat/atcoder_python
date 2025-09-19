# 高さと横幅が偶数の場合は、2x2のブロックの個数を計算する
# h, w = 1 のパターンも考慮する

h, w = map(int, input().split())

# 特殊ケース：HかWが1の場合は、全てのマスにライトを置く
if h == 1 or w == 1:
    print(h * w)

# 一般ケース：H, Wがともに1より大きい場合
else:
    # 必要なライトの行数
    rows_needed = (h + 1) // 2

    # 必要なライトの列数
    cols_needed = (w + 1) // 2

    print(rows_needed * cols_needed)

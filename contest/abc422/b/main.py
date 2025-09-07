h, w = map(int, input().split())
s = [input() for _ in range(h)]

flag = True

for i in range(h):
    for j in range(w):

        # .ならスルー
        if s[i][j] == ".":
            continue

        # 縦横のどちらかに隣接する#の数を数える
        count = 0
        if h == 1 and w == 1:
            print("No")
            exit()

        elif h == 1 and w > 1:
            if j == 0:
                if s[i][j+1] == "#":
                    count += 1
            elif j == w-1:
                if s[i][j-1] == "#":
                    count += 1
            else:
                if s[i][j+1] == "#":
                    count += 1
                if s[i][j-1] == "#":
                    count += 1
        elif w == 1 and h > 1:
            if i == 0:
                if s[i+1][j] == "#":
                    count += 1
            elif i == h-1:
                if s[i-1][j] == "#":
                    count += 1
            else:
                if s[i+1][j] == "#":
                    count += 1
                if s[i-1][j] == "#":
                    count += 1
        elif h > 1 and w > 1:
            if i == 0:
                if j == 0:
                    if s[i+1][j] == "#":
                        count += 1
                    if s[i][j+1] == "#":
                        count += 1
                elif j == w-1:
                    if s[i+1][j] == "#":
                        count += 1
                    if s[i][j-1] == "#":
                        count += 1
                else:
                    if s[i+1][j] == "#":
                        count += 1
                    if s[i][j+1] == "#":
                        count += 1
                    if s[i][j-1] == "#":
                        count += 1
            elif i == h-1:
                if j == 0:
                    if s[i-1][j] == "#":
                        count += 1
                    if s[i][j+1] == "#":
                        count += 1
                elif j == w-1:
                    if s[i-1][j] == "#":
                        count += 1
                    if s[i][j-1] == "#":
                        count += 1
                else:
                    if s[i-1][j] == "#":
                        count += 1
                    if s[i][j+1] == "#":
                        count += 1
                    if s[i][j-1] == "#":
                        count += 1
            elif j == 0:
                if s[i+1][j] == "#":
                    count += 1
                if s[i-1][j] == "#":
                    count += 1
                if s[i][j+1] == "#":
                    count += 1
            elif j == w-1:
                if s[i+1][j] == "#":
                    count += 1
                if s[i-1][j] == "#":
                    count += 1
                if s[i][j-1] == "#":
                    count += 1
            else:
                if s[i+1][j] == "#":
                    count += 1
                if s[i-1][j] == "#":
                    count += 1
                if s[i][j+1] == "#":
                    count += 1
                if s[i][j-1] == "#":
                    count += 1

        if s[i][j] == "#" and count != 2 and count != 4:
            flag = False
            print("No")
            exit()

print("Yes")

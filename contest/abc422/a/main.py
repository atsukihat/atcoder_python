i, j = map(int, input().split("-"))

if i <= 8 and j != 8:
    print(str(i) + "-" + str(j+1))
elif i < 8 and j == 8:
    print(str(i+1) + "-" + str(1))
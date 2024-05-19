h = int(input())

hight = 0

for i in range(0, 1000):
    hight += 2**i
    if (h < hight):
        print(i+1)
        break
N = int(input())
card = [list(map(int, input().split())) for card in range(N)]

discard_set = set()

for i in range(N-1):
    for j in range(i+1, N):
        if (j in discard_set or i in discard_set):
            continue
        if ((card[i][0] > card[j][0]) & (card[i][1] < card[j][1])):
            discard_set.add(j)
        elif ((card[i][0] < card[j][0]) & (card[i][1] > card[j][1])):
            discard_set.add(i)
            
strength_card = list(i+1 for i in range(N) if i not in discard_set)
        
print(len(strength_card))
print(*strength_card)


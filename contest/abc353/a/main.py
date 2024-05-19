N = int(input())
h = list(map(int, input().split()))

result = -1

first_building_height = h[0]

for i in range(1, N):
    if (h[i] > first_building_height):
        result = i+1
        break
    
print(result)
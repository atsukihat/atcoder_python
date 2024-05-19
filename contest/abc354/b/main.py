N = int(input())

list = []
total_rate = 0

for i in range(N):
    s, c = input().split()
    list.append([s, int(c)])

for i in range(N):
    total_rate += list[i][1]

mod_result = total_rate % len(list)

sorted_list = sorted(list)

print(sorted_list[mod_result][0])

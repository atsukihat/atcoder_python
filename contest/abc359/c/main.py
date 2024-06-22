S_x, S_y = map(int, input().split())
T_x, T_y = map(int, input().split())

if (S_x + S_y) % 2 == 1:
    S_x -= 1
if (T_x + T_y) % 2 == 1:
    T_x -= 1

# 通行料
traffic_fee = 0

# 移動量
# M_yの通行料は必ずかかる。
M_x = abs(T_x - S_x)
M_y = abs(T_y - S_y)

diagonal = M_x - M_y


if diagonal <= 0:
    traffic_fee = M_y
else:
    traffic_fee = M_y + (diagonal // 2)

print(traffic_fee)
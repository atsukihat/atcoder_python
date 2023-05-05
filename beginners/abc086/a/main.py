a, b = map(int, input().split())  # map関数は第一引数に任意の関数（型）、第二引数以降にiterabel(リスト、文字列など)
print("Even" if a*b % 2 == 0 else "Odd")  # 三項演算子を用いている

# a,b = list(map(int,input().split()))
# if a*b%2==0:
#   print("Even")
# else:
#   print("Odd")

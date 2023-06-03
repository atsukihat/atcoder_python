N = int(input())
S = input()
a_count = S.count('A')
t_count = S.count('T')
if (a_count > t_count):
    print('A')
elif (t_count > a_count):
    print('T')
else:
    if (S[-1] == 'A'):
        print('T')
    else:
        print('A')

n = int(input())
result = []


# 2^n に該当する`{`または`}`で構成される文字列を全列挙する関数
def generate_all(current):
    if len(current) == n:
        result.append(current)
    else:
        generate_all(current + '(')
        generate_all(current + ')')


# 列挙された`{`と`}`の文字列が条件を満たすかを判定する関数
def is_valid(s):
    left = 0
    right = 0

    for c in s:
        if c == '(':
            left += 1
        else:
            right += 1

        if right > left:
            return False

    return left == right


def main():

    if n % 2 == 1:
        print()

    generate_all('')

    for s in result:
        if is_valid(s):
            print(s)


main()
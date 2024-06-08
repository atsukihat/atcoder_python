# 再帰関数を使って解く
N = int(input())

# まずは、N=1の場合を考える
# N = 1
default = [
    "###",
    "#.#",
    "###"
]


# N = 2以降の場合用いる再帰関数
def recursive(n):
    if n == 0:
        return ['#']
    elif n == 1:
        return default
    else:
        prev = recursive(n-1)
        new = []
        size = len(prev)
        
        # 上段
        for row in prev:
            new.append(row*3)
        
        # 中段
        for row in prev:
            new.append(row + '.' * size + row)
            
        # 下段
        for row in prev:
            new.append(row*3)

    return new
  
  
result = recursive(N)

print(result)

for line in result:
    print(line)
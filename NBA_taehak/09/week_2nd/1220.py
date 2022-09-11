# 1220. Magnetic

for case in range(1, 11):

    # 1: n극 2: s극
    size = int(input())
    table = [input().split() for _ in range(size)]

    result = 0
    for col in range(size):
        memo = ['2']
        for row in range(size):
            magnet = table[row][col]
            if magnet == '0':
                continue
            if magnet != memo[-1]:
                memo.append(magnet)
        if memo[-1] == '1':
            memo.pop()

        result += (len(memo) - 1) // 2

    print(f'#{case} {result}')

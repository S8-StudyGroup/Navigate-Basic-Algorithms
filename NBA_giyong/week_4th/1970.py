# 쉬운 거스름돈

import sys

sys.stdin = open("input")

t = int(input())

for tc in range(1, t + 1):
    n = int(input())

    result = []
    if n // 50000:
        result.append(n//50000)
        n = n - n//50000 * 50000
    else:
        result.append(0)

    if n // 10000:
        result.append(n//10000)
        n = n - n // 10000 * 10000
    else:
        result.append(0)

    if n // 5000:
        result.append(n//5000)
        n = n - n // 5000 * 5000
    else:
        result.append(0)

    if n // 1000:
        result.append(n//1000)
        n = n - n // 1000 * 1000
    else:
        result.append(0)

    if n // 500:
        result.append(n//500)
        n = n - n // 500 * 500
    else:
        result.append(0)

    if n // 100:
        result.append(n//100)
        n = n - n // 100 * 100
    else:
        result.append(0)

    if n // 50:
        result.append(n//50)
        n = n - n // 50 * 50
    else:
        result.append(0)

    if n // 10:
        result.append(n//10)
        n = n - n // 10 * 10
    else:
        result.append(0)

    print(f"#{tc}")
    print(*result)


    # money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    # cnt = [0] * 8

    # for i in range(8):
    #     cnt[i] = n // money[i]
    #     n %= money[i]

    # print(f"#{tc}")
    # print(*cnt)
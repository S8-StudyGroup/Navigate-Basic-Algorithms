# 쉬운 거스름돈

money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for t in range(1, int(input()) + 1):
    price = int(input())

    change = [0] * 8

    for i, v in enumerate(money):
        change[i] = price // v
        price = price % v

    print(f'#{t}')
    print(*change)
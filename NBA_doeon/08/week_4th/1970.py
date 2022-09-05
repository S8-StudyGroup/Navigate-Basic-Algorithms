# 쉬운 거스름돈

for tc in range(1, int(input()) + 1):
    money = int(input())

    standard = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = []

    for i in standard:
        if money // i != 0:
            result.append(money // i)
        else:
            result.append(0)

        money -= i * (money // i) 

    print(f'#{tc}')
    print(*result)

# 쉬운 거스름돈

# 돈 종류
moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for case in range(1, int(input()) + 1):

    # 거스름돈
    change = int(input())

    result = []

    for money in moneys:
        result.append(change // money)
        change %= money

    print(f'#{case}')
    print(*result)

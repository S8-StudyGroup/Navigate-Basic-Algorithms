# 쉬운 거스름돈

T = int(input())

for test_case in range(1, T + 1):

    N = int(input())

    total = []
    money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    for money in money_list:
        total.append(N // money)
        N = N % money

    print(f"#{test_case}")
    print(*total)

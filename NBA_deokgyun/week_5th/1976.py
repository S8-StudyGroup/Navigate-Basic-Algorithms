# 시각 덧셈

for test_case in range(1, int(input()) + 1):
    clock_list = list(map(int, input().split()))
    print(
        f"#{test_case}",
        sum(clock_list[::2]) % 12 + sum(clock_list[1::2]) // 60,
        sum(clock_list[1::2]) % 60,
    )

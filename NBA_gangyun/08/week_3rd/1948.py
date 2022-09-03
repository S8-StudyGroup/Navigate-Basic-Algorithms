# 날짜 계산기

month_info = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

for test_case in range(1, int(input()) + 1):
    calculate_month = 0
    calculate_day = 0
    result = 0
    date_info = list(map(int, input().split()))

    for i in range(date_info[0], date_info[2]):
        calculate_month += month_info[i]

    calculate_day = date_info[3] - date_info[1] + 1
    result = calculate_month + calculate_day

    print(f'#{test_case} {result}')

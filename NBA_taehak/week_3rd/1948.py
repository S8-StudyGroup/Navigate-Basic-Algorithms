# 날짜 계산기

import sys

sys.stdin = open('input_1948.txt')

date = {
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

for case in range(1, int(input()) + 1):
    month_1, day_1, month_2, day_2 = map(int, input().split())

    day = day_2 - day_1 + 1
    for i in range(month_2 - month_1):
        day += date[(month_1 + i - 1) % 12 + 1]

    print(f'#{case} {day}')

# 날짜 계산기

import sys

sys.stdin = open("input.txt")

month_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

T = int(input())

for test_count in range(1, T + 1):
    date_list = list(map(int, input().split()))

    date1 = sum(month_list[: date_list[0]]) + date_list[1]
    date2 = sum(month_list[: date_list[2]]) + date_list[3]

    print(f"#{test_count}", date2 - date1 + 1)

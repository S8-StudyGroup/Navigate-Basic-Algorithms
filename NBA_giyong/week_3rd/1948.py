# 날짜 계산기
import sys

sys.stdin = open("input.txt")

data = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t = int(input())
for tc in range(1, t + 1):
    month, day, next_month, next_day = map(int, input().split())
    result = 0
    if month == next_month:
        result += next_day - day + 1
    else:
        result += next_day
        for j in range(next_month-1, month, -1):
            result += data[j]
        result += data[month] - day + 1

    print(f"#{tc} {result}")
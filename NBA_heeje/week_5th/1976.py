# 시각 덧셈

# 시각 덧셈

T = int(input())

for test_case in range(1, T + 1):

    hour = 0
    min = 0

    fir_hour, fir_min, sec_hour, sec_min = map(int, input().split())

    min += fir_min + sec_min

    if min >= 60:
        min -= 60
        hour += 1

    hour += fir_hour + sec_hour

    if hour > 12:
        hour -= 12

    print(f'#{test_case} {hour} {min}')

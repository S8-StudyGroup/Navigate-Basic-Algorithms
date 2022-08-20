# 날짜 계산기

# 달에 따른 일수를 담은 리스트
days_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 총 테스트 케이스의 개수
T = int(input())

for test_case in range(1, T + 1):
    month1, day1, month2, day2 = map(int, input().split())

    # 일수 계산
    total_day = 0

    for i in range(month1, month2):

        # 달에 따른 일수를 더한다.
        total_day += days_of_month[i]

    # 나머지 일을 더한다.
    total_day += day2 - day1 + 1

    print(f'#{test_case} {total_day}')

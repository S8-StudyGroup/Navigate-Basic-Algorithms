# 1952. [모의 SW 역량테스트] 수영장

import sys
sys.stdin = open('input.txt')


for test_case in range(1, int(input()) + 1):
    ticket = list(map(int, input().split()))
    month_plan = list(map(int, input().split()))
    sum_money = 0
    i = 0

    for start in range(12):
        if month_plan[start] != 0:
            i = start
            break

    while i < 12:
        three_months = month_plan[i:i + 3]
        three_months_money = 0
        month_money = 0
        for days in three_months[::-1]:
            if ticket[1] < days * ticket[0]:
                three_months_money += ticket[1]
                month_money = ticket[1]
            else:
                three_months_money += days * ticket[0]
                month_money = days * ticket[0]

        if ticket[2] < three_months_money:
            i += 3
            sum_money += ticket[2]
        else:
            i += 1
            sum_money += month_money

    if ticket[3] < sum_money:
        sum_money = ticket[3]
    print(f'#{test_case} {sum_money}')

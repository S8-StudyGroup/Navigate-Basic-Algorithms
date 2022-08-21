# 날짜 계산기

for t in range(1, int(input()) + 1):

    last_date = {
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
        12: 31
    }

    two_dates = list(map(int, input().split()))

    m, d = two_dates[0], two_dates[1]
    cnt = 0
    while True:
        cnt += 1

        if m == two_dates[2] and d == two_dates[3]:
            break

        # 해당 월의 마지막 날에 도달하면
        if d == last_date[m]:
            m += 1
            d = 1  # 1일로 초기화
            continue
        d += 1

    print(f'#{t} {cnt}')


# swea 1952. [모의 SW 역량테스트]수영장

# dp - bottom-up
for case in range(1, int(input()) + 1):

    # 순서대로 1일, 1개월, 3개월, 1년 이용권 요금
    prices = list(map(int, input().split()))
    plan = [0] + list(map(int, input().split()))

    # 1월부터 해당 월 까지의 최소 요금을 계속 구함
    dp = [0] * 13
    for m in range(1, 13):

        # 월마다 계산
        # 1~m월 까지 최소 요금 = (m-1)월 까지 요금 + min(해당 월 1일 요금 * 이용일, 1개월 요금)
        dp[m] = dp[m - 1] + min(prices[0] * plan[m], prices[1])

        # 3월 부터는 3개월 요금과도 비교
        if m >= 3:
            dp[m] = min(dp[m], dp[m - 3] + prices[2])

        # 12월 일 때 1년요금과 비교
        if m == 12:
            dp[m] = min(dp[m], prices[3])

    print(f'#{case} {dp[-1]}')

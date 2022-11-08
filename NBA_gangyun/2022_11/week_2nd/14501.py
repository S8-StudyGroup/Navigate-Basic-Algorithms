# BOJ_14501. 퇴사

freedom = int(input())
meeting = [list(map(int, input().split())) for _ in range(freedom)]
dp = [0] * (freedom + 1)  # 퇴사 날짜 = N + 1

for day in range(freedom - 1, -1, -1):
    if day + meeting[day][0] > freedom:  # 해당 상담이 끝나는 날이 퇴사 날짜를 넘어가는 경우
        dp[day] = dp[day + 1]  # 상담을 할 수 없는 날이므로, dp 값을 변화 없이 이전 날로 넘긴다.

    else:  # 상담 일이 긴 경우, 상담이 끝나는 날짜의 dp와 해당 상담일을 더해서 새로운 dp를 만들어 비교
        compare = dp[day + meeting[day][0]] + meeting[day][1]
        if compare > dp[day + 1]:  # 비교 값이 크면 dp를 최신화
            dp[day] = compare
        else:  # 비교 값이 작으면 이전 dp 값을 그대로 사용
            dp[day] = dp[day + 1]

print(max(dp))  # dp 요소들 중 최대값을 출력

# [BOJ] 14501. 퇴사

# 전기버스2와 비슷!

def dfs(day, cur_profit):
    if day == N + 1:                    # 종료조건 : 남은 일을 모두 소진했다면
        global max_profit
        if max_profit < cur_profit:     # 저장된 최대 수익과 현재 수익을 비교
            max_profit = cur_profit
        return

    next_day = day + schedule[day][0]   # 현재 일자의 상담을 수락했을 때 다음 상담을 받을 수 있는 날짜
    if next_day <= N + 1:               # 남은 일 안에 끝낼 수 있는 상담일 경우
        dfs(next_day, cur_profit + schedule[day][1])    # 상담을 받은 경우로 dfs 진행
    dfs(day + 1, cur_profit)            # 상담을 받지 않은 경우로 dfs 진행


N = int(input())
schedule = [[]]
max_profit = 0
for _ in range(N):
    schedule.append(list(map(int, input().split())))

dfs(1, 0)
print(max_profit)

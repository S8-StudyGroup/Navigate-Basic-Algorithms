# [BOJ] 14501. 퇴사


def dfs(day, profit):  # 현재 날짜, 현재까지 얻은 수익
    global max_profit

    if day == n:  # 모든 날짜를 다 돌았다면
        if profit > max_profit:  # max값 갱신 후 중단
            max_profit = profit
        return
    else:  # 아직 진행 중이라면
        if (
            day + plan[day][0] <= n
        ):  # 현재 날짜에 상담 걸리는 일자를 더 했을 때 n보다 작거나 같다면(즉, 퇴사 전 가능하다면)
            dfs(
                day + plan[day][0], profit + plan[day][1]
            )  # 1) 현재 날짜 상담을 진행하는 경우, 수익을 그만큼 더함
        dfs(day + 1, profit)  # 2) 현재 날짜 상담을 패스하고 다음 날짜를 보러가는 경우


n = int(input())
plan = [[] for _ in range(n)]
max_profit = 0

for i in range(n):
    plan[i] = list(
        map(int, input().split())
    )  # [[걸리는 시간, 수익], [걸리는 시간, 수익], ...] 형태로 저장

dfs(0, 0)  # 0번째 날짜, 수익은 0으로 시작
print(max_profit)

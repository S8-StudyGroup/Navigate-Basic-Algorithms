# [BOJ] 14501. 퇴사


def dfs(day, cur_profit):
    if day == N + 1:
        global max_profit
        if max_profit < cur_profit:
            max_profit = cur_profit
        return

    next_day = day + schedule[day][0]
    if next_day <= N + 1:
        dfs(next_day, cur_profit + schedule[day][1])
    dfs(day + 1, cur_profit)


N = int(input())
schedule = [[]]
max_profit = 0
for _ in range(N):
    schedule.append(list(map(int, input().split())))

dfs(1, 0)
print(max_profit)

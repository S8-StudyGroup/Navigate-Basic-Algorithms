# [SWEA] 1952. [모의 SW 역량테스트] 수영장
# Guest - 오태훈


def day_or_month(month_idx):
    day_cost = plan[month_idx] * prices[0]
    month_cost = prices[1]
    return min(day_cost, month_cost)


for t in range(1, int(input()) + 1):
    prices = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    total_cost = [0] * 13
    for i in range(1, 13):
        total_cost[i] = total_cost[i - 1] + day_or_month(i - 1)
        if i >= 3:
            month_3 = (
                total_cost[i - 3] + prices[2]
            )  # 1일권 / 1달권 비교한 누적값 , 3개월전 누적값  + 3개월권
            total_cost[i] = min(total_cost[i], month_3)
    year_or_total = min(prices[3], total_cost[12])
    print(f'#{t} {year_or_total}')

# DFS

# def dfs(cost, month):
#     global min_cost
#     if month > 12:
#         min_cost = min(min_cost, cost)
#         return
#     # 1일권
#     dfs(cost + plan[month] * prices[0], month + 1)
#     # 1달권
#     dfs(cost + prices[1], month + 1)
#     # 3달권
#     dfs(cost + prices[2], month + 3)

# for t in range(1, int(input()) + 1):
#     prices = list(map(int, input().split()))
#     plan = [0] + list(map(int, input().split()))
#     min_cost = prices[3]
#     dfs(0, 1)
#     print(f'#{t} {min_cost}')

# [BOJ] 14501. 퇴사
from collections import defaultdict


dday = int(input())
schedule = defaultdict()
schedule[0] = (1, 0)
schedule[dday + 1] = (1, 0)
for day in range(1, dday + 1):
    schedule[day] = tuple(map(int, input().split()))    # (take time, money)
earn = [-1] * (dday + 2)


def dfs(node=0, mymoney=0):

    if node > dday + 1:
        return

    if mymoney > earn[node]:
        earn[node] = mymoney
    else:
        return
    
    for next_node in range(node + schedule[node][0], dday + 2):
        next_money = mymoney + schedule[node][1]
        # print((next_node, next_money), earn)
        dfs(next_node, next_money)


dfs()
print(earn[-1])

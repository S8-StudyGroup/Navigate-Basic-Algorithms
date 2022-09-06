# 1952. [모의 SW 역량테스트] 수영장

import sys

sys.stdin = open("sample_input.txt")

# dfs로 해결한다
def dfs_swim(month, now_sum):
    # 1년 플랜을 최소값으로 설정해둔다
    global min_price_sum
    # 현재의 깊이에서 합이 최소보다 커지면 가망성이 없으므로 잘라낸다
    if now_sum > min_price_sum:
        return
    # 아닐경우 지금의 달이 12보다 크다면 이미 전부 플랜을 정했으므로 최소값을 갱신한다
    elif month > 12:
        if now_sum < min_price_sum:
            min_price_sum = now_sum
        return
    # 전부 아닐 경우 더 깊이 dfs를 시행해서 들어간다
    else:
        dfs_swim(month + 1, now_sum + how_many_use[month] * plans[0])
        dfs_swim(month + 1, now_sum + plans[1])
        dfs_swim(month + 3, now_sum + plans[2])


for test_count in range(1, int(input()) + 1):
    plans = list(map(int, input().split()))
    how_many_use = [0] + list(map(int, input().split()))
    # 최소값은 단 하나의 경우의 수 밖에는 없는 1년 플랜을 넣어둔다
    min_price_sum = plans[3]
    dfs_swim(0, 0)
    print(f"#{test_count}", min_price_sum)

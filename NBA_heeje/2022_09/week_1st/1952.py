# 1952. [모의 SW 역량테스트] 수영장

# v : 현재 월
# cur_price : 현재 누적 가격
def dfs(v, cur_price):
    global min_price

    # 현재 가격이 최소 가격보다 클 경우 가지치기
    if cur_price >= min_price:
        return

    # 모든 경우를 다 탐색했을 때 현재 가격과 최소 가격 비교
    if v == 13:
        if cur_price < min_price:
            min_price = cur_price
        return

    # 1일 이용권 사용
    dfs(v + 1, cur_price + prices[0] * plan[v])

    # 1달 이용권 사용
    dfs(v + 1, cur_price + prices[1])

    # 3달 이용권 사용
    if v <= 10:
        dfs(v + 3, cur_price + prices[2])


T = int(input())

for tc in range(1, T + 1):
    prices = list(map(int, input().split()))
    plan = [0] + list(map(int, input().split()))

    # 최소 가격을 1년 이용권으로 초기화
    min_price = prices[-1]

    dfs(1, 0)

    print(f"#{tc} {min_price}")

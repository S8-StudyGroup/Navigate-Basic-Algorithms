# [BOJ] 15686. 치킨 배달

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

# 1. 치킨집과 집의 좌표 구하기
chicken = []
house = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])
# print(chicken)
# print(house)

# 2. 각 집에서 모든 치킨집까지의 맨하탄 거리 구하기
distance = []
for hx, hy in house:
    dis = []
    for cx, cy in chicken:
        dis.append(abs(cx - hx) + abs(cy - hy))
    distance.append(dis)
# print(distance)


idx = list(range(len(chicken)))         # 치킨집 번호 리스트 (좌표 대신 번호로)
answer = 100000


# 3. 가능한 치킨집 조합 중 가장 최소 치킨거리를 지니는 치킨집을 뽑기
def comb(arr=[], start=0):
    global answer

    if len(arr) == m:
        sum_dis = 0
        for k in range(len(distance)):          # 각 집별로
            min_dis = 1000
            for j in arr:
                if distance[k][j] < min_dis:    # 해당 치킨집들까지의 거리 중
                    min_dis = distance[k][j]    # 가장 최소값을 찾아서 더해줌
            sum_dis += min_dis
        if sum_dis < answer:                    # 가능한 조합의 경우 중
            answer = sum_dis                    # 가장 최소거리를 구해줌
        return

    for i in range(start, len(chicken)):        # 조합 구하는 코드
        arr.append(idx[i])
        comb(arr, i + 1)
        arr.pop()


comb()
print(answer)
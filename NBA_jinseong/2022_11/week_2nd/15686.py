# [BOJ] 15686. 치킨 배달
# 대실패

# 도시크기 N x N
# 0: 빈칸, 1: 집, 2: 치킨집
# 치킨집 개수는 최대 M개

# idea
# 치킨 집 위치 다 받아오기
# 그중에 M개 골라서 치킨 거리 구하기
# 최소값나올때까지 다찾기
# 각집에 대해서 치킨 거리 구하기

def chicken(start, houses):
    global chicken_distance

    if len(houses) == M:
        for normal_house in normal_houses:
            distances = []
            normal_r, normal_c = normal_house
            for chicken_house in chicken_houses:
                chicken_r, chicken_c = chicken_house
                distance = abs(chicken_r - normal_r) + abs(chicken_c - normal_c)
                distances.append(distance)
            distances.append(min(distances))
        min_distance = min(distances)
        if min_distance < chicken_distance:
            chicken_distance = min_distance
        return

    if start >= len(chicken_houses):
        return
    # 고르기
    houses.append(chicken_houses[start])
    chicken(start + 1, houses)
    houses.pop()
    # 안고르기
    chicken(start + 1, houses)


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

chicken_houses = []
normal_houses = []
for i in range(N):                          # 집들 위치 받아오기
    for j in range(N):
        if city[i][j] == 1:
            normal_houses.append([i, j])
        if city[i][j] == 2:
            chicken_houses.append([i, j])

chicken_distance = N * N * len(normal_houses)

chicken(0, [])

print(chicken_distance)

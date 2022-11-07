# [BOJ] 15686. 치킨 배달

# 도시에 있는 치킨집 중에서 최대 M개를 고르라고 하였지만, 도시의 치킨 거리가 가장 작게 되는 경우를 구하는 거라면
# 무조건 M개를 고르는게 치킨 거리가 가장 작다!

from itertools import combinations

N, M = map(int, input().split())

matrix = []
houses = []
stores = []
min_total_distance = 9999
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:                 # 집의 위치만 따로 houses라는 리스트에 저장
            houses.append((i, j))
        elif row[j] == 2:               # 치킨집의 위치만 따로 stores라는 리스트에 저장
            stores.append((i, j))
    matrix.append(row)

for survive_stores in combinations(range(len(stores)), M):  # 모든 치킨집에서 M개만 고르는 조합
    total_distance = 0                                      # 도시의 치킨 거리
    for house_x, house_y in houses:                         # 모든 집에 대하여
        min_distance = 100
        for store in survive_stores:                        # 골라놓은 치킨집들과의 거리를 측정
            store_x, store_y = stores[store]
            distance = abs(house_x - store_x) + abs(house_y - store_y)
            if min_distance > distance:                     # 가장 작은 거리값 저장하여
                min_distance = distance
        total_distance += min_distance                      # 총 거리값에 더한다.
    if min_total_distance > total_distance:                 # 해당 경우의 수로 나오는 총 거리값과
        min_total_distance = total_distance                 # 저장되어있는 총 거리값 비교

print(min_total_distance)

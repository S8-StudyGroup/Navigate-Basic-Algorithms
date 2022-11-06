# [BOJ] 15686. 치킨 배달

from itertools import combinations

N, M = map(int, input().split())

matrix = []
houses = []
stores = []
min_total_distance = 9999
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            houses.append((i, j))
        elif row[j] == 2:
            stores.append((i, j))
    matrix.append(row)

for survive_stores in combinations(range(len(stores)), M):
    total_distance = 0
    for house_x, house_y in houses:
        min_distance = 100
        for store in survive_stores:
            store_x, store_y = stores[store]
            distance = abs(house_x - store_x) + abs(house_y - store_y)
            if min_distance > distance:
                min_distance = distance
        total_distance += min_distance
    if min_total_distance > total_distance:
        min_total_distance = total_distance

print(min_total_distance)

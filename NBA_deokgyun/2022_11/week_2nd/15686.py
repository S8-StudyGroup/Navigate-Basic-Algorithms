# [BOJ] 15686. 치킨 배달

import itertools

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
house = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i,j))
houselen = len(house)
chickenlen = len(chicken)
house_chicken = [[] for _ in range(houselen)]
eachhouse = 0
for h in house:
    for c in chicken:
        house_chicken[eachhouse].append(abs(h[0] - c[0]) + abs(h[1] - c[1]))
    eachhouse += 1
minchickendist = 10**6
for open in itertools.combinations(range(chickenlen), m):
    chickendist = 0
    for i in range(houselen):
        mindist = 10**6
        for j in open:
            if house_chicken[i][j] < mindist:
                mindist = house_chicken[i][j]
        chickendist += mindist
    if chickendist < minchickendist:
        minchickendist = chickendist
print(minchickendist)
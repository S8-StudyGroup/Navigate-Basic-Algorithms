# [BOJ] 20058. 마법사 상어와 파이어스톰

import sys
from collections import deque

input = sys.stdin.readline
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def melt_checker(ice):
    melt_points = []
    for i in range(ice_size):
        for j in range(ice_size):
            melt_count = 0
            for direction in range(4):
                check_i = i + di[direction]
                check_j = j + dj[direction]
                if (
                        0 <= check_i < ice_size and 0 <= check_j < ice_size
                        and ice[check_i][check_j] != 0
                ):
                    melt_count += 1

            if melt_count < 3 and ice[i][j] > 0:
                melt_points.append((i, j))

    return melt_points


def fire_storm(ice):
    for power in power_list:
        magic_power = 2 ** power
        divide = ice_size // magic_power
        new_ice = [[] for _ in range(ice_size)]
        for i in range(divide):
            for j in range(divide):
                storm = [[] for _ in range(magic_power)]
                for r_i in range(magic_power):
                    for r_j in range(magic_power):
                        storm[r_i].append(ice[i * magic_power + r_i][j * magic_power + r_j])
                rotated_storm = list(map(list, zip(*storm[::-1])))
                for col in range(magic_power):
                    for k in rotated_storm[col]:
                        new_ice[i * magic_power + col].append(k)

        ice = new_ice
        for point in melt_checker(ice):
            ice[point[0]][point[1]] -= 1

    return ice


def bfs(i, j):
    remain_ice = 1
    visited[i][j] = True
    queue = deque()
    queue.append((i, j))

    while queue:
        i, j = queue.popleft()
        for direction in range(4):
            check_i = i + di[direction]
            check_j = j + dj[direction]
            if (
                    0 <= check_i < ice_size and 0 <= check_j < ice_size
                    and not visited[check_i][check_j]
                    and ice[check_i][check_j] > 0
            ):
                remain_ice += 1
                visited[check_i][check_j] = True
                queue.append((check_i, check_j))

    return remain_ice


N, Q = map(int, input().split())
ice_size = 2 ** N
ice = [list(map(int, input().split())) for _ in range(ice_size)]
power_list = list(map(int, input().split()))
result = 0
ice = fire_storm(ice)

for i in range(ice_size):
    for j in range(ice_size):
        if ice[i][j] > 0:
            result += ice[i][j]

max_ice = 0
visited = [[False] * ice_size for _ in range(ice_size)]
for i in range(ice_size):
    for j in range(ice_size):
        if ice[i][j] > 0 and not visited[i][j]:
            max_ice = max(bfs(i, j), max_ice)

print(result)
print(max_ice)
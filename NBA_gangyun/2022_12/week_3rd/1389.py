# [BOJ] 1389. 케빈 베이컨의 6단계 법칙
from collections import deque


def bfs(start, end, depth):
    visited[start] = True
    queue = deque()
    queue.append((start, depth))

    while queue:
        start, depth = queue.popleft()
        if start == end:
            break
        for next_friend in graph[start]:
            if not visited[next_friend]:
                visited[next_friend] = True
                queue.append((next_friend, depth + 1))

    return depth


N, M = map(int, input().split())
relation = [list(map(int, input().split())) for _  in range(M)]

graph = [[] for _ in range(N + 1)]
for v1, v2 in relation:
    graph[v1].append(v2)
    graph[v2].append(v1)

min_kv_num = N * M
result = 0
for start in range(1, N + 1):
    kv_num = 0
    for end in range(1, N + 1):
        if start != end:
            depth = 0
            visited = [False for _ in range(N + 1)]
            kv_num += bfs(start, end, 0)

    if kv_num < min_kv_num:
        min_kv_num = kv_num
        result = start

print(result)
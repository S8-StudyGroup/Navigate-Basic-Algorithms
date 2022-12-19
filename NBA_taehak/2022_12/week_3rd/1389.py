# [BOJ] 1389. 케빈 베이컨의 6단계 법칙
from collections import deque
import sys
input = sys.stdin.readline

node_cnt, edge_cnt = map(int, input().split())

graph = [[] for _ in range(node_cnt + 1)]
for _ in range(edge_cnt):
    a, b = map(int ,input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    kevin = [0] * (node_cnt + 1)
    visited = set()
    que = deque()

    visited.add(start)
    que.append(start)

    while que:
        node = que.popleft()
        for n_node in graph[node]:
            if n_node not in visited:
                kevin[n_node] = kevin[node] + 1
                visited.add(n_node)
                que.append(n_node)
    
    return sum(kevin)


min_kevin = 9999
answer = -1
for node_num in range(1, node_cnt + 1):
    node_kevin = bfs(node_num)
    if node_kevin < min_kevin:
        min_kevin = node_kevin
        answer = node_num
print(answer)


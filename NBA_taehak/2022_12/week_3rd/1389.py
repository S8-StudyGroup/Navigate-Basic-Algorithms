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

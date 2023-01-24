# [BOJ] 2206. 벽 부수고 이동하기

import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 6)

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

# def dfs(y, x, step, break_brick):
#     global min_step

#     visited[y][x] = True

#     if y == N - 1 and x == M - 1:
#         if min_step > step:
#             min_step = step
#         return
    
#     if step >= min_step:
#         return
    
#     for d in range(4):
#         move_y, move_x = y + dy[d], x + dx[d]
#         if 0 <= move_y < N and 0 <= move_x < M and not visited[move_y][move_x]:
#             if matrix[move_y][move_x] == '0':
#                 dfs(move_y, move_x, step + 1, break_brick)
#             else:
#                 if not break_brick:
#                     matrix[move_y][move_x] = '0'
#                     break_brick = True
#                     dfs(move_y, move_x, step + 1, break_brick)
#                     break_brick = False
#                     matrix[move_y][move_x] = '1'

#     visited[y][x] = False

from collections import deque

def bfs():
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    queue = deque([(0, 0, 0)]) 

    while queue:
        y, x, break_brick = queue.popleft()

        if y == N - 1 and x == M - 1:
            return visited[y][x][break_brick]

        for d in range(4):
            move_y, move_x = y + dy[d], x + dx[d]
            if 0 <= move_y < N and 0 <= move_x < M:
                if matrix[move_y][move_x] == '0' and visited[move_y][move_x][break_brick] == 0:
                    visited[move_y][move_x][break_brick] = visited[y][x][break_brick] + 1
                    queue.append((move_y, move_x, break_brick))
                elif matrix[move_y][move_x] == '1' and break_brick == 0:
                    visited[move_y][move_x][break_brick + 1] = visited[y][x][break_brick] + 1
                    queue.append((move_y, move_x, not break_brick))

    return -1

N, M = map(int, input().split())
matrix = [list(str(input().rstrip())) for _ in range(N)]
# dfs(0, 0, 1, False)
print(bfs())
# [BOJ] 2638. 치즈

from collections import deque
import sys
input = sys.stdin.readline


dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def bfs(start):
    '''
    외곽과 연결된 곳은 전부 3으로 바꾸는 bfs
    '''
    que = deque([start])
    area[start[0]][start[1]] = 3

    while que:
        r, c = que.popleft()
        for di in range(4):
            nr = r + dr[di]
            nc = c + dc[di]
            if 0 <= nr < r_size and 0 <= nc < c_size and area[nr][nc] == 0:
                area[nr][nc] = 3
                que.append((nr, nc))


def is_diappear(start):
    '''
    상하좌우 2칸 이상이 3인경우(외곽공기) True
    '''
    r, c = start
    count = 0
    for di in range(4):
        nr = r + dr[di]
        nc = c + dc[di]
        if 0 <= nr < r_size and 0 <= nc < c_size and area[nr][nc] == 3:
            count += 1
    
    if count >= 2:
        return True
    else:
        return False


r_size, c_size = map(int, input().split())
area = [list(map(int ,input().split())) for _ in range(r_size)]

# 테두리에서 bfs, 치즈 좌표저장
cheeze_list = []
for r in range(r_size):
    for c in range(c_size):
        if (r in [0, r_size - 1] or c in [0, c_size - 1]) and area[r][c] == 0:
            bfs((r, c))
        if area[r][c] == 1:
            cheeze_list.append((r, c))

# 치즈가 없을 때 까지 반복
time = 0
while cheeze_list:
    # 남아있게될 치즈 좌표, 사라지는 치즈 좌표
    cheeze_left = []
    cheeze_disappear = []
    for cheeze in cheeze_list:
        if is_diappear(cheeze):
            cheeze_disappear.append(cheeze)
        else:
            cheeze_left.append(cheeze)

    # 치즈가 없어지면서 뚫리는 공간까지 바꾸기위해 bfs
    for cheeze in cheeze_disappear:
        bfs(cheeze)

    # 시간 경과, 남아있는 치즈로 치즈리스트 갱신
    time += 1
    cheeze_list = cheeze_left

print(time)
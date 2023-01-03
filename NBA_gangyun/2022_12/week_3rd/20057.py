# [BOJ] 20057. 마법사 상어와 토네이도
from collections import deque

# 좌 하 우 상
di_spiral = [0, 1, 0, -1]
dj_spiral = [-1, 0, 1, 0]

# 상 좌 하 우
di_sand1 = deque([-1, 0, 1, 0])
dj_sand1 = deque([0, -1, 0, 1])

# 좌상 좌하 우하 우상
di_sand2 = deque([-1, 1, 1, -1])
dj_sand2 = deque([-1, -1, 1, 1])

# 상2 좌2 하2 우2
di_sand3 = deque([-2, 0, 2, 0])
dj_sand3 = deque([0, -2, 0, 2])


# 토네이도의 이동
def spiral(i, j, direction, start):
    # 지금 향하고 있는 방향으로 좌표를 1칸 옮기고
    i += di_spiral[direction]
    j += dj_spiral[direction]
    
    # 일정 비율로 모래를 흩날리는 함수 실행
    move_sand(i, j, direction)
    return i, j, start + 1


# 토네이도의 방향이 바뀔 때 모래의 이동방향도 바꿔주는 함수
def rotate_direction():
    di_sand1.rotate(-1)
    di_sand2.rotate(-1)
    di_sand3.rotate(-1)
    dj_sand1.rotate(-1)
    dj_sand2.rotate(-1)
    dj_sand3.rotate(-1)


# 모래의 이동
def move_sand(i, j, plus_d):
    total_sand = grid[i][j]
    grid[i][j] = 0
    remain_sand = total_sand
    
    # 상, 하, 좌, 우에 있는 모래를 이동
    for direction in range(4):
        if direction == 0 or direction == 2:
            k = 0.07
        else:
            continue
        sand_i = i + di_sand1[direction]
        sand_j = j + dj_sand1[direction]
        sand_part = int(total_sand * k)
        if 0 <= sand_i < N and 0 <= sand_j < N:
            grid[sand_i][sand_j] += sand_part
        remain_sand -= sand_part

    # 대각선 좌상, 좌하, 우상, 우하에 있는 모래를 이동
    for direction in range(4):
        if direction == 0 or direction == 1:
            k = 0.1
        else:
            k = 0.01
        sand_i = i + di_sand2[direction]
        sand_j = j + dj_sand2[direction]
        sand_part = int(total_sand * k)
        if 0 <= sand_i < N and 0 <= sand_j < N:
            grid[sand_i][sand_j] += sand_part
        remain_sand -= sand_part
    
    # 상2, 좌2, 하2에 있는 모래를 이동
    for direction in range(4):
        if direction == 0 or direction == 2:
            k = 0.02
        elif direction == 1:
            k = 0.05
        else:
            continue
        sand_i = i + di_sand3[direction]
        sand_j = j + dj_sand3[direction]
        sand_part = int(total_sand * k)
        if 0 <= sand_i < N and 0 <= sand_j < N:
            grid[sand_i][sand_j] += sand_part
        remain_sand -= sand_part
    
    # 비율 a의 칸으로 남아있는 모래를 이동
    if 0 <= i + di_spiral[plus_d] < N and 0 <= j + dj_spiral[plus_d] < N:
        grid[i + di_spiral[plus_d]][j + dj_spiral[plus_d]] += remain_sand


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

total = sum(map(sum, grid))
i, j = N // 2, N // 2       # 격자의 가운데부터 시작
direction = 0               # 초기의 방향(왼쪽)
start, end = 0, 1

while True:
    if i == 0 and j == 0:
        break
    i, j, start = spiral(i, j, direction, start)
    if start == end:
        start = 0
        direction = (direction + 1) % 4
        rotate_direction()
        if direction % 2 == 0:      # 방향이 2번 바뀌면 토네이도의 길이가 1 증가
            end += 1

remain_sand = sum(map(sum, grid))
print(total - remain_sand)
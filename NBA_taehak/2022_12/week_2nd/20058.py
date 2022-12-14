# [BOJ] 20058. 마법사 상어와 파이어스톰

import sys
input = sys.stdin.readline
limit_number = 15000
sys.setrecursionlimit(limit_number)


# N 격자 크기 2^(N) , Q 단계
N, Q = map(int, input().split())
table_size = 2 ** N

# table 정보
table = [list(map(int, input().split())) for _ in range(table_size)]

# 단계별 L
fire_size = list(map(int, input().split()))


# 시계방향으로 90도 회전 하는 함수
def rotate_90(cell):
    return list(zip(*cell[::-1]))


# 테이블을 크기 L 부분 격자로 나누고 회전 시키는 함수
def divide_and_rotate(table, L):

    if L == 0:
        return

    cell_size = 2 ** L

    for x in range(0, table_size, cell_size):
        for y in range(0, table_size, cell_size):
            temp = [[0] * cell_size for _ in range(cell_size)]
            for i in range(cell_size):
                for j in range(cell_size):
                    temp[i][j] = table[x+i][y+j]
            temp = rotate_90(temp)
            for i in range(cell_size):
                for j in range(cell_size):
                    table[x+i][y+j] = temp[i][j]


# 인접 얼음 개수 구하고 -1 해주는 함수
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def melt(table):
    melting = []

    for r in range(table_size):
        for c in range(table_size):
            near_ice_cnt = 0
            for di in range(4):
                nr = r + dr[di]
                nc = c + dc[di]
                if 0 <= nr < table_size and 0 <= nc < table_size and table[nr][nc] > 0:
                    near_ice_cnt += 1
            if near_ice_cnt < 3:
                melting.append((r, c))
    
    for r, c in melting:
        if table[r][c] == 0:
            continue
        table[r][c] -= 1


# 남아있는 얼음의 합
for L in fire_size:
    divide_and_rotate(table, L)
    melt(table)

print(sum(map(sum, table)))

# for i in table:
#     print(i)


# 가장큰 덩어리 구하기
def dfs(r, c):
    global mass_cnt

    table[r][c] = -1
    mass_cnt += 1
    
    for di in range(4):
        nr = r + dr[di]
        nc = c + dc[di]
        if 0 <= nr < table_size and 0 <= nc < table_size and table[nr][nc] > 0:
            dfs(nr, nc)


max_mass = 0
for r in range(table_size):
    for c in range(table_size):
        if table[r][c] > 0:
            mass_cnt = 0
            dfs(r, c)

            if mass_cnt > max_mass:
                max_mass = mass_cnt

print(max_mass)
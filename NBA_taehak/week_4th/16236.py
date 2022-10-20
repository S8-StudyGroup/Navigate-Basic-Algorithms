# [BOJ] 16236. 아기 상어
import sys
input = sys.stdin.readline


board_size = int(input())
board = [list(map(int, input().split())) for _ in range(board_size)]
baby_size = 2

# 상어 위치 찾기, 상어 위치한 곳은 0으로 바꿔주기
baby = tuple()
for r in range(board_size):
    for c in range(board_size):
        if board[r][c] == 9:
            board[r][c] = 0
            baby = (r, c)


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def bfs(baby):
    visited = [[False] * board_size for _ in range(board_size)]
    visited[baby[0]][baby[1]] = True
    check_list = [baby]
    stop = False
    time = 0
    fishes = []
    while True:
        time += 1

        memo = []
        while check_list:
            r, c = check_list.pop()
            for di in range(4):
                nr = r + dr[di]
                nc = c + dc[di]

                if 0 <= nr < board_size and 0 <= nc < board_size and not visited[nr][nc] and board[nr][nc] <= baby_size:
                    visited[nr][nc] = True
                    memo.append((nr, nc))

                    if 0 < board[nr][nc] < baby_size:
                        stop = True
                        fishes.append((nr, nc))
        
        if stop:
            fishes.sort(key=lambda x: x[1])
            fishes.sort()
            return fishes[0], time
        
        if not memo:
            return False, time
        
        check_list = memo


result = 0
eat = 0
while True:
    next_loc, time = bfs(baby)
    baby = next_loc

    if not next_loc:
        break
    
    eat += 1
    if eat == baby_size:
        baby_size += 1
        eat = 0
    result += time
    board[baby[0]][baby[1]] = 0
    

    # for i in board:
    #     print(i)
    # print('total :', result, ',time :', time, ',baby_size :', baby_size, ',eat :', eat, ',now :', baby)
    # print()

print(result)

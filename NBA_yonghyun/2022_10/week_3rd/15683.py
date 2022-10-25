# [BOJ] 15683. 감시

import sys

input = sys.stdin.readline

# 시계방향 (상 -> 우 -> 하 -> 좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cctv_dir = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
    5: [[0, 1, 2, 3]],
}


def view(x, y, num, cnt=1):
    global blank
    global min_blank

    dir = cctv_dir.get(num)

    for i in range(len(dir)):
        for d in dir[i]:
            nx = x
            ny = y
            # print(x, y)
            while 0 <= nx + dx[d] < n and 0 <= ny + dy[d] < m:  # 조건 만족하면 그 방향으로 계속
                nx, ny = nx + dx[d], ny + dy[d]
                if office[nx][ny] == 0:  # 빈 칸
                    office[nx][ny] = '#' * cnt
                    blank -= 1
                elif office[nx][ny] == 6:
                    break
        if cctv:
            next_x, next_y, next_num = cctv.pop()
            view(next_x, next_y, next_num, cnt + 1)
            # print(next_x, next_y)
            for d in dir[i]:
                nx = x
                ny = y
                while 0 <= nx + dx[d] < n and 0 <= ny + dy[d] < m:
                    nx, ny = nx + dx[d], ny + dy[d]
                    if office[nx][ny] == '#' * cnt:
                        office[nx][ny] = 0
                        blank += 1
                    elif office[nx][ny] == 6:
                        break

        else:
            if blank < min_blank:
                min_blank = blank
                # for k in range(n):
                #     print(office[k])
                # print()

            for d in dir[i]:
                nx = x
                ny = y
                while 0 <= nx + dx[d] < n and 0 <= ny + dy[d] < m:
                    nx, ny = nx + dx[d], ny + dy[d]
                    if office[nx][ny] == '#' * cnt:
                        office[nx][ny] = 0
                        blank += 1
                    elif office[nx][ny] == num:
                        break

    cctv.append([x, y, num])


n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]
cctv = []
blank = 0
min_blank = m * n
for i in range(n):
    for j in range(m):
        if office[i][j] in range(1, 6):
            cctv.append([i, j, office[i][j]])
        elif office[i][j] == 0:
            blank += 1

# print(office)
# print(cctv)
if cctv:
    x, y, num = cctv.pop()
    view(x, y, num)
    print(min_blank)
else:
    print(blank)

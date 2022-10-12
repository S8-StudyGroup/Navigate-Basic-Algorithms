# [BOJ] 7576. 토마토

# 0이 있는지 검사
# -1로 막힌 부분이 있는지 검사하기'


def bfs(li):
    global cnt

    next_arr = []
    for l in li:
        x, y = l
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < M and 0 <= ny < N and (tomatoes[nx][ny] == 0):
                tomatoes[nx][ny] = 1
                next_arr.append([nx, ny])

    if not next_arr:
        return
    else:
        cnt += 1
        bfs(next_arr)


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

M, N = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(N)]

arr = []                            # [[1, 2], [2, 3]]
cnt = 0
for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            arr.append([i, j])

bfs(arr)

result = cnt
if 0 in tomatoes:
    result = -1

print(result)




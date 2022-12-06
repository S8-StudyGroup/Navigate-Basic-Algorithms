# [BOJ] 7569. 토마토(3차원)

# 토마토(3차원)
import sys
from collections import deque

input = sys.stdin.readline


def bfs(ripe_tomatoes):                     # ripe_tomatoes: 익은 토마토 리스트
    cnt_ripe_tomatoes = len(ripe_tomatoes)  # 익은 토마토의 개수 저장
    queue = deque(ripe_tomatoes)            # 큐(덱)에 익은 토마토 리스트 저장
    day = 0                                 # 지난 날짜 수
    while queue:                            # 덱이 비워질 때까지 진행
        day += 1                            # 날짜 + 1
        for _ in range(len(queue)):         # 현재 큐의 길이만큼만 진행(날짜 계산을 위해서!)
            z, x, y = queue.popleft()
            for d in range(6):              # 탐색해야 하는 개수는 6개(상, 하, 좌, 우, z축위, z축아래)
                move_z, move_x, move_y = z + dz[d], x + dx[d], y + dy[d]  # 탐색 위치

                # 해당 탐색 위치가 유효성 검사를 통과하고 익지 않은 토마토이면
                if 0 <= move_z < H and 0 <= move_x < N and 0 <= move_y < M and matrix[move_z][move_x][move_y] == 0:
                    matrix[move_z][move_x][move_y] = 1      # 해당 토마토를 익은 토마토로 변환
                    cnt_ripe_tomatoes += 1                  # 익은 토마토 + 1
                    queue.append((move_z, move_x, move_y))  # 큐에 삽입

        # 잘 되어 있나 확인 테스트
        # for p1 in range(H):
        #     for p2 in range(N):
        #         print(matrix[p1][p2])
        #     print()
        # print()

    # 모든 작업을 완료한 후

    if cnt_ripe_tomatoes == cnt_tomatoes:   # 모든 토마토가 다 익었다면
        return day - 1                      # day - 1 반환(모두 다 익은 시점에서 while문이 한 번 더 돌아가기 때문)
    else:                                   # 익지 않은 토마토가 존재한다면
        return -1                           # -1 반환


# 3차원 델타탐색
dx = [-1, 0, 1, 0, 0, 0]
dy = [0, -1, 0, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

M, N, H = map(int, input().split())
cnt_tomatoes = M * N * H                # 총 토마토 개수
ripe_tomatoes = []                      # 익은 토마토 리스트
matrix = []                             # 토마토 리스트

for i in range(H):
    box = []  # 토마토 한 박스
    for j in range(N):
        row = list(map(int, input().split()))  # 토마토 한 줄
        for k in range(M):
            if row[k] == -1:                        # 토마토가 들어있지 ㅇ낳다면
                cnt_tomatoes -= 1                   # 총 토마토 개수 - 1
            elif row[k] == 1:                       # 익은 토마토라면
                ripe_tomatoes.append((i, j, k))     # 익은 토마토 리스트에 좌표 저장
        box.append(row)                             # 박스에 한 줄 저장
    matrix.append(box)                              # 토마토 리스트에 박스 저장

if len(ripe_tomatoes) == cnt_tomatoes:              # 익은 토마토의 개수와 총 토마토 개수가 같다면
    print(0)                                        # 0을 출력
else:                                               # 그렇지 않다면
    print(bfs(ripe_tomatoes))                       # 익은 토마토 리스트로 bfs 실행

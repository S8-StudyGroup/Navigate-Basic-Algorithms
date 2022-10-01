# [SWEA] 1211. Ladder2

import sys
sys.stdin = open('input.txt')

# 우 하 좌
dx = [0, 1, 0]
dy = [1, 0, -1]


for test_case in range(1, 11):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    min_count = 100 * 100
    start_point = 0

    # 사다리의 첫 행을 순회하며 시작지점(== 1로 표시된 곳)을 찾는다.
    for i in range(100):
        if ladder[0][i] == 1:                               # 시작지점을 찾았다면
            visited = [[False] * 100 for _ in range(100)]   # 방문 표시를 위한 2차원 배열 생성
            x = 0                                           # x = 0일 때부터 시작
            y = i                                           # y = i일 때부터 시작
            start_point = y                                 # 시작점의 y 좌표를 저장
            count = 0                                       # 이동거리를 카운트할 변수 생성

            # 출구를 찾을 때까지 수행
            while x != 99:
                # 델타 검색
                for direction in range(3):
                    nx = x + dx[direction]
                    ny = y + dy[direction]
                    # nx, ny가 사다리의 범위 내에 있고, 사다리가 이어져 있고, 방문하지 않은 경우
                    if 0 <= nx < 100 and 0 <= ny < 100 and ladder[nx][ny] == 1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        count += 1
                        x, y = nx, ny
            # 이동 거리의 최소값 비교
            if count < min_count:
                result = start_point    # 이동 거리가 최소일 때의 시작지점을 결과에 저장
                min_count = count

    print(f'#{test_case} {result}')

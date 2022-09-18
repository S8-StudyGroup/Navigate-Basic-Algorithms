# [SWEA] 1211. Ladder2
#

import sys

sys.stdin = open('1211.txt')

# 델타 [아래, 왼쪽, 오른쪽]
d_r = [1, 0, 0]
d_c = [0, -1, 1]

# 사다리 실행 함수
def ladder(col, row=0, direction=0, distance=1):

    # 시작위치:(0, col) 방향: 0
    while row < 99:
        # 방향으로 한칸 이동
        row += d_r[direction]
        col += d_c[direction]
        distance += 1

        # 방향 변화
        # 방향이 아래방향 일때
        if direction == 0:

            # 왼쪽 확인 후 갈 수 있다면 방향 변화
            if 0 <= col - 1 < 100 and area[row][col - 1] == 1:
                direction = 1
            # 오른쪽 확인 후 ~
            elif 0 <= col + 1 < 100 and area[row][col + 1] == 1:
                direction = 2

        # 방향이 왼쪽 오른쪽 일때
        elif direction in [1, 2]:

            # 아래방향 확인 후 ~
            if area[row + 1][col] == 1:
                direction = 0

    return distance


for case in range(1, 11):
    casenum = int(input())
    area = [list(map(int, input().split())) for _ in range(100)]

    # 최소 이동 거리, x
    min_distance = 10000
    x = 0

    # 시작점 찾고 사다리 실행
    for start_col in range(100):
        if area[0][start_col] == 1:
            distance = ladder(start_col)

            # 최소값 갱신
            if distance < min_distance:
                min_distance = distance
                x = start_col

    print(f'#{case} {x}')

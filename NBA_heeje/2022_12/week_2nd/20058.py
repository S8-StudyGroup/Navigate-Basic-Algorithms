# [BOJ] 20058. 마법사 상어와 파이어스톰

import sys

input = sys.stdin.readline

# 델타탐색
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 2차원 리스트를 회전시키는 함수
def rotate_matrix():
    rotate_x = 0  # 회전시킬 x좌표
    while rotate_x < two_power_N:
        rotate_y = 0  # 회전시킬 y좌표
        while rotate_y < two_power_N:
            before_rotate = []  # 회전할 구역을 추출해올 리스트
            for i in range(two_power_L):  # 회전할 구역 추출
                before_rotate.append(
                    matrix[rotate_x + i][rotate_y : rotate_y + two_power_L]
                )

            # 추출한 리스트를 90도 회전
            after_rotate = [
                [row[i] for row in before_rotate[::-1]]
                for i in range(len(before_rotate[0]))
            ]

            # 회전한 2차원 리스트를 다시 matrix의 같은 구역에 집어넣기
            for i in range(two_power_L):
                matrix[rotate_x + i][rotate_y : rotate_y + two_power_L] = after_rotate[
                    i
                ]
            rotate_y += two_power_L
        rotate_x += two_power_L


# 얼음의 양을 줄이는 함수
# 얼음이 녹는 과정은 동시에 처리되기 때문에 녹는 위치를 저장해뒀다가 한번에 처리
def reduce_ice_amount():
    reduce_ice_amount_list = []  # 얼음이 녹는 위치 저장
    for x in range(two_power_N):  # 전체 탐색
        for y in range(two_power_N):
            if matrix[x][y] != 0:  # 얼음이 있는 곳이라면 탐색 시작
                cnt = 0  # 인접 얼음 개수
                for d in range(4):  # 인접한 부분을 탐색하여
                    move_x, move_y = x + dx[d], y + dy[d]
                    if (  # 유효성 검사를 통과하고
                        0 <= move_x < two_power_N  # 얼음이 존재할 경우
                        and 0 <= move_y < two_power_N
                        and matrix[move_x][move_y] != 0
                    ):
                        cnt += 1  # 인접 얼음 + 1
                else:
                    if cnt < 3:  # 인접 얼음이 3개 이하일 경우
                        reduce_ice_amount_list.append((x, y))  # 얼음이 줄어들 예정인 리스트에 추가

    for reduce_x, reduce_y in reduce_ice_amount_list:  # 전체 탐색이 끝난 후
        matrix[reduce_x][reduce_y] -= 1  # 해당 구역들에 얼음 - 1


# 전체 얼음의 개수를 구하는 함수
def get_total_ice():
    return sum([sum(matrix[i]) for i in range(two_power_N)])


# 가장 큰 얼음 덩어리를 구하는 함수
def get_cnt_of_biggest_ice_area():
    max_cnt = 0
    visited = [[False] * two_power_N for _ in range(two_power_N)]
    for x in range(two_power_N):  # 전체 탐색
        for y in range(two_power_N):
            if not visited[x][y] and matrix[x][y] != 0:  # 얼음이 존재하고 방문하지 않은 곳이라면
                cur_cnt = 1  # BFS 실행
                visited[x][y] = True  # 초기값 작업
                queue = [(x, y)]
                while queue:  # 큐가 빌 때까지 진행
                    cur_x, cur_y = queue.pop(0)  # 현재 위치 선정
                    for d in range(4):  # 델타 탐색
                        move_x, move_y = cur_x + dx[d], cur_y + dy[d]  # 탐색 위치 선정
                        if (
                            0 <= move_x < two_power_N  # 유효성 검사를 통과하고
                            and 0 <= move_y < two_power_N
                            and not visited[move_x][move_y]  # 방문하지 않았으며
                            and matrix[move_x][move_y] != 0  # 얼음이 있을 경우
                        ):
                            cur_cnt += 1  # 붙어있는 얼음 개수 + 1
                            visited[move_x][move_y] = True  # 방문 처리
                            queue.append((move_x, move_y))  # 큐에 삽입

                if max_cnt < cur_cnt:  # 붙어있는 얼음 개수와 최대 얼음 개수
                    max_cnt = cur_cnt  # 비교 및 갱신
    return max_cnt  # 최대 얼음 덩어리 반환


N, Q = map(int, input().split())
two_power_N = 2**N  # 2의 N승 값 미리 저장
matrix = [list(map(int, input().split())) for _ in range(two_power_N)]
L_list = list(map(int, input().split()))

for L in L_list:  # 각 단계마다 작업 실행
    two_power_L = 2**L  # 단계에 따른 2의 L값 미리 저장
    rotate_matrix()  # 배열 회전 함수 실행
    reduce_ice_amount()  # 얼음 양 줄이는 함수 실행

# 얼음의 총 개수와 최대 얼음 덩어리의 양 출력
print(get_total_ice(), get_cnt_of_biggest_ice_area(), sep="\n")

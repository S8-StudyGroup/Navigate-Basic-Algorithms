# [Programmers] 77485. 행렬 테두리 회전하기

def solution(rows, columns, queries):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    answer = []

    # 1부터 rows * columns까지의 숫자가 순서대로 적힌 2차원 행렬을 생성하되, 편의를 위해
    # 왼쪽과 위쪽에 0을 담은 행 및 열 생성
    # 예시) rows = 4, columns = 4일 때,
    # 0  0  0  0  0
    # 0  1  2  3  4
    # 0  5  6  7  8
    # 0  9 10 11 12
    # 0 13 14 15 16
    matrix = [[0] + [columns * i + j for j in range(1, columns + 1)] for i in range(rows)]
    matrix.insert(0, [0] * (columns + 1))

    for query in queries:                           # 각각의 회전 케이스
        x, y = query[0], query[1]                   # 맨 왼쪽 위 좌표
        temp = matrix[x][y]                         # 값을 임시 저장할 변수
        min_num = temp                              # 최소 숫자 값 저장
        for d in range(4):                                                              # 시계 방향 탐색
            move_x, move_y = x + dx[d], y + dy[d]                                       # 탐색 위치 지정
            while query[0] <= move_x <= query[2] and query[1] <= move_y <= query[3]:    # 해당 방향으로 회전 케이스의 범위 밖으로 나갈 때까지
                matrix[move_x][move_y], temp = temp, matrix[move_x][move_y]             # 임시 변수와 해당 위치 값 swap
                min_num = min(min_num, temp)                                            # 최소 숫자 값도 함께 비교 및 갱신
                move_x += dx[d]                                                         # 해당 방향으로 x값 이동
                move_y += dy[d]                                                         # 해당 방향으로 y값 이동
            else:                                                                       # while문을 통해 범위 밖으로 나갔다면
                x, y = move_x - dx[d], move_y - dy[d]                                   # 한칸 되돌려서 범위 안으로 넣기!
        # for k in range(rows + 1):
        #     print(matrix[k])
        answer.append(min_num)                      # 해당 회전 케이스에서의 최소 값을 answer에 삽입
    return answer                                   # answer 출력

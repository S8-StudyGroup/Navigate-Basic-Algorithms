# [Programmers] 87694. 아이템 줍기


def solution(rectangle, characterX, characterY, itemX, itemY):

    # 델타탐색
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    def bfs(start_y, start_x):         # start_y: 캐릭터의 Y좌표 / start_x: 캐릭터의 X좌표
        queue = [(start_y, start_x)]
        while queue:
            y, x = queue.pop(0)

            for d in range(4):
                move_y, move_x = y + dy[d], x + dx[d]
                if move_x == itemX * 2 and move_y == itemY * 2:
                    return board[y][x] // 2                         # 두 배 해줬으니 나누기 2해준다!

                if (
                    2 <= move_y <= 100                              # 유효성 검사 통과하고
                    and 2 <= move_x <= 100
                    and board[move_y][move_x] == 1                  # 가지 않은 길이면
                ):
                    board[move_y][move_x] = board[y][x] + 1         # 해당 위치 값을 +1 해주고 queue에 넣어준다.
                    queue.append((move_y, move_x))

    board = [[0] * 101 for _ in range(101)]         # 보드판 및 모든 좌표에 2를 곱한다.(이유는 그림으로 설명)

    for x1, y1, x2, y2 in rectangle:                # 직사각형의 모서리와 내부 모두 1을 넣어준다.
        for y in range(y1 * 2, y2 * 2 + 1):
            for x in range(x1 * 2, x2 * 2 + 1):
                board[y][x] = 1

    for x1, y1, x2, y2 in rectangle:                # 직사각형의 내부만 0로 바꿔준다.
        for y in range(y1 * 2 + 1, y2 * 2):
            for x in range(x1 * 2 + 1, x2 * 2):
                board[y][x] = 0

    return bfs(characterY * 2, characterX * 2)

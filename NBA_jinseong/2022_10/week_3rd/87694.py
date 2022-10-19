# [Programmers] 87694. 아이템 줍기

# rectangle = [좌측하단x,좌측하단y, 우측상단x, 우측하단y]
# idea
# 모서리에 숫자 표기 다하기 1로 -> 1만 따라가면 됨
# 그다음 중복되는 모서리 지우기 위해서 모서리말고 안쪽이면 0으로 다시 채우기

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue = [[x, y]]
    while queue:
        x, y = queue.pop(0)             # 가장 첨 저장한 좌표부터 pop

        for d in range(4):



def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    board = [[0] * 51 for _ in range(51)]       # 1~50

    for x1, y1, x2, y2 in rectangle:
        for x in range(x1, x2 + 1):             # 가생이 처리
            board[x][y1] = 1
            board[x][y2] = 1
        for y in range(y1, y2 + 1):
            board[x1][y] = 1
            board[x2][y] = 1
    for x1, y1, x2, y2 in rectangle:            # 중복되는 너비는 다 0으로
        for x in range(x1 + 1, x2):
            for y in range(y1 + 1, y2):
                board[x][y] = 0


    return answer

# [Programmers] 87694. 아이템 줍기

# 아이템줍기
'''
좌표값 1 ~ 50
좌하단, 우상단 좌표
'''

def solution(rectangle, characterX, characterY, itemX, itemY):


    def draw(box):
        x1, y1, x2, y2 = map(lambda x: 2*x, box)
        
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                board[x][y] = 7


    board = [[0] * 104 for _ in range(104)]
    for box in rectangle:
        draw(box)
    
    d_x = [1, 0, -1, 0]
    d_y = [0, -1, 0, 1]
    distance = 0
    x_now, y_now = 2*characterX, 2*characterY
    di_now = 0

    for di in range(4):

        next_x = x_now + d_x[di]
        next_y = y_now + d_y[di]
        next_x_2 = next_x + d_x[(di + 1) % 4]
        next_y_2 = next_y + d_y[(di + 1) % 4]
        next_x_3 = next_x_2 + d_x[(di + 2) % 4]
        next_y_3 = next_y_2 + d_y[(di + 2) % 4]
        if board[next_x][next_y] == 7 and board[next_x_2][next_y_2] == 0:
            x_now = next_x
            y_now = next_y
            distance += 1
            di_now = di
            break
        elif board[next_x][next_y] == 7 and board[next_x_2][next_y_2] == 7 and board[next_x_3][next_y_3] == 0:
            x_now = next_x
            y_now = next_y
            distance += 1
            di_now = di
            break
    
    while (x_now, y_now) != (2*characterX, 2*characterY):
        # print((x_now, y_now), distance)
        if (x_now, y_now) == (2*itemX, 2*itemY):
            memo = distance

        for di in range(4):
            if di == di_now + 2:
                continue

            next_x = x_now + d_x[di]
            next_y = y_now + d_y[di]
            next_x_2 = next_x + d_x[(di + 1) % 4]
            next_y_2 = next_y + d_y[(di + 1) % 4]
            next_x_3 = next_x_2 + d_x[(di + 2) % 4]
            next_y_3 = next_y_2 + d_y[(di + 2) % 4]
            if board[next_x][next_y] == 7 and board[next_x_2][next_y_2] == 0:
                x_now = next_x
                y_now = next_y
                distance += 1
                di_now = di
                break
            elif board[next_x][next_y] == 7 and board[next_x_2][next_y_2] == 7 and board[next_x_3][next_y_3] == 0:
                x_now = next_x
                y_now = next_y
                distance += 1
                di_now = di
                break
    
    answer = min(distance - memo, memo)
    return answer // 2


# rr = [[1,1,5,7]]
# cx = 1
# cy = 1
# ix = 4
# iy = 7

rr = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
cx = 1
cy = 3
ix = 7
iy = 8

print(solution(rr, cx, cy, ix, iy))
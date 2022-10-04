# 120861 캐릭터의 좌표
def solution(keyinput, board):
    # 최대 최소값
    max_x = board[0] // 2
    max_y = board[1] // 2
    min_x = -max_x
    min_y = -max_y

    # 초기위치
    x = y = 0

    # 진행
    for key in keyinput:
        if key == 'left':
            if x > min_x:
                x -= 1
        elif key == 'right':
            if x < max_x:
                x += 1
        elif key == 'up':
            if y < max_y:
                y += 1
        else:
            if y > min_y:
                y -= 1

    answer = [x, y]
    return answer
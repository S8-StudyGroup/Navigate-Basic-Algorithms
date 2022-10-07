# [Programmers] 120861. 캐릭터의 좌표


def solution(keyinput, board):
    start = [0, 0]
    garo = board[0] // 2
    sero = board[1] // 2
    for i in keyinput:
        if i == 'left':
            a = start[0] + (-1)
            b = start[1] + 0
            if -garo <= a <= garo and -sero <= b <= sero:
                start[0], start[1] = a, b
        if i == 'right':
            a = start[0] + 1
            b = start[1] + 0
            if -garo <= a <= garo and -sero <= b <= sero:
                start[0], start[1] = a, b
        if i == 'up':
            a = start[0] + 0
            b = start[1] + 1
            if -garo <= a <= garo and -sero <= b <= sero:
                start[0], start[1] = a, b
        if i == 'down':
            a = start[0] + 0
            b = start[1] + -1
            if -garo <= a <= garo and -sero <= b <= sero:
                start[0], start[1] = a, b

    answer = start
    return answer

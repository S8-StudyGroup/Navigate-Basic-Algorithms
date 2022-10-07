# [Programmers] 120861번 캐릭터의 좌표
# board = [가로크기, 세로크기] -> 둘다 홀수

key = {
    'up': [0, 1],
    'down': [0, -1],
    'left': [-1, 0],
    'right': [1, 0]
}


def solution(keyinput, board):

    width, length = board                   # 가로 세로 정하기
    w_value, l_value = width // 2, length // 2          # x축, y축 최대절대값
    start = [0, 0]                          # 시작점 정하기
    x, y = start
    for k in keyinput:                      # 각 키값에 따라 이동
        dx, dy = key[k]
        nx, ny = x + dx, y + dy
        if -w_value <= nx <= w_value and -l_value <= ny <= l_value:
            x, y = nx, ny

    answer = [x, y]
    return answer
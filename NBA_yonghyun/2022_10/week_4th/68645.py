# [Programmers] 68645. 삼각 달팽이

dx = [1, 0, -1]
dy = [-1, 2, -1]  # 왼쪽 이동의 경우, 2칸씩 이동


def solution(n):
    snails = [[0] * 2 * n for _ in range(n)]  # 2n X n 크기의 배열 생성

    d = 0  # 달팽이의 이동 방향
    num = 1  # 입력할 숫자
    nx = -1
    ny = n
    while n > 0:  # 최대한 숫자를 다 채울 때까지
        k = n
        while k > 0:
            nx, ny = nx + dx[d], ny + dy[d]
            snails[nx][ny] = num
            num += 1  # 입력할 숫자는 하나씩 늘려주고
            k -= 1  # 이동거리는 줄여줌
        d += 1
        if d == 3:  # 3가지 방향으로 전부 이동했다면,
            d = 0  # 다시 처음 방향으로 (왼쪽 아래 대각선)
        n -= 1  # 각 방향으로 n에서 -1씩 줄인 거리만큼 이동

    result = []
    for snail in snails:
        for i in snail:
            if i != 0:  # 0을 제외한 숫자들을 리스트에 담음
                result.append(i)
    return result


solution(6)

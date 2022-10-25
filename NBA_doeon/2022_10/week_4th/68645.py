# [Programmers] 68645. 삼각 달팽이


def solution(n):
    answer = []

    dx = [1, 0, -1]  # 왼쪽아래, 오른쪽, 왼쪽위 방향 순서의 델타값
    dy = [-1, 2, -1]

    arr = [[0] * (n * 2 - 1) for _ in range(n)]  # 한 칸씩 띄워진 이차원 리스트
    strike = 0  # 달팽이 종료 조건을 위한 변수 - strike 3개 달성 시 break

    # 1. 시작 설정값
    x = 0
    y = n - 1
    d = 0  # 처음 방향
    value = 1  # 처음 값
    arr[x][y] = value  # 값을 해당 위치에 채우고 시작

    # 2. 값 채우기 작업
    while True:
        x = x + dx[d % 3]  # 현재 진행 중인 방향으로 다음 칸 접근
        y = y + dy[d % 3]

        # 2-1) 그 다음 칸이 범위 밖이거나 이미 값이 채워져있다면(0이 아니면)
        if x < 0 or x >= n or y < 0 or y >= (n * 2 - 1) or arr[x][y] != 0:
            x -= dx[d % 3]  # 다시 돌아와주고
            y -= dy[d % 3]
            d += 1  # 방향 바꿈
            strike += 1  # 현재 방향이 안 됐으므로 strike 1개 추가

        # 2-2) 다음칸이 채울 수 있는 값이면
        elif 0 <= x < n and 0 <= y < (n * 2 - 1) and arr[x][y] == 0:
            strike = 0  # strike는 초기화해주고
            value += 1  # 이전 칸의 값보다 +1 한 값을
            arr[x][y] = value  # 달팽이에 채움

        # 2-3) 모든 방향(3방향)에 대해서 strike를 기록한 경우 -> 더 이상 값을 채울 필요 없음
        if strike >= 3:
            break

    # 값 채우기 완료 후, 이차원리스트 순회로 0이 아닌 값만 answer에 저장
    for i in range(n):
        for j in range(n * 2 - 1):
            if arr[i][j] != 0:
                answer.append(arr[i][j])

    return answer

# SWEA - 4013. [모의 SW 역량테스트] 특이한 자석
# Guest - 이용준

from collections import deque


def rotation(num, di):
    rotated[num] = True  # 현재 자석 회전 여부 True 처리

    if 0 <= num - 1 < 4 and not rotated[num - 1]:  # 양옆 자석 번호가 범위 내이고 회전을 안했다면
        if magnetics[num][6] != magnetics[num - 1][2]:  # 회전 가능한 경우만
            rotation(num - 1, -di)  # 재귀적으로 회전 실행

    if 0 <= num + 1 < 4 and not rotated[num + 1]:
        if magnetics[num][2] != magnetics[num + 1][6]:
            rotation(num + 1, -di)

    magnetics[num].rotate(di)  # 덱의 rotate 함수로 간단히 회전 실행!


for tc in range(1, int(input()) + 1):
    k = int(input())
    magnetics = [
        deque(map(int, input().split())) for _ in range(4)
    ]  # 회전에 용이하게 덱으로 자석 구현

    for _ in range(k):
        number, direction = map(int, input().split())
        number -= 1

        rotated = [False] * 4  # 회전 여부를 체크할 리스트
        rotation(number, direction)  # 회전 실행

    result = 0
    for i in range(4):
        if magnetics[i][0] == 1:  # 빨간 화살표가 위치한 날이 S극인 경우만
            result += 2**i  # 규칙에 맞게 점수 더해주기

    print(f'#{tc} {result}')

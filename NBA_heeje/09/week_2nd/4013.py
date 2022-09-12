# 4013. 특이한 자석


def turn_gear(idx, d):
    visited[idx] = True  # 이미 회전한 자석을 다시 회전시키는 일을 방지하기 위함

    if (
        1 <= idx - 1  # 해당 자석의 왼쪽에 자석이 있고,
        and not visited[idx - 1]  # 그 자석이 회전한 적이 없으면서
        and gear_list[idx][6] != gear_list[idx - 1][2]  # 자석끼리 맞닿아 있는 부분이 다른 극일 경우
    ):  # 해당 자석을 반대 방향으로 돌린다.
        turn_gear(idx - 1, -d)

    if (
        idx + 1 <= 4  # 해당 자석의 오른쪽에 자석이 있고,
        and not visited[idx + 1]  # 그 자석이 회전한 적이 없으면서
        and gear_list[idx][2] != gear_list[idx + 1][6]  # 자석끼리 맞닿아 있는 부분이 다른 극일 경우
    ):  # 해당 자석을 반대 방향으로 돌린다.
        turn_gear(idx + 1, -d)

    if d == 1:  # 시계 방향으로 회전
        gear_list[idx].insert(0, gear_list[idx].pop())
    if d == -1:  # 반시계 반향으로 회전
        gear_list[idx].append(gear_list[idx].pop(0))


T = int(input())

for tc in range(1, T + 1):

    K = int(input())
    score = 0
    gear_list = [[]]  # 1번 자석부터 4번 자석까지의 정보를 담는 리스트(0번은 편의상 비워둠)
    for _ in range(4):
        gear_list.append(list(map(int, input().split())))

    for _ in range(K):  # 자석을 회전시키는 반복문
        int_mag, dir = list(map(int, input().split()))
        visited = [False] * 5  # 방문 리스트는 매 반복마다 초기화시켜줘야 한다!
        turn_gear(int_mag, dir)

    # 모든 회전을 마친 후 점수 계산
    for i in range(1, 5):
        if gear_list[i][0] == 1:  # 빨간색 화살표 위치에 있는 날의 자성이 S극인 경우
            score += 2 ** (i - 1)

    print(f"#{tc} {score}")

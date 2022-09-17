# [SWEA] 1211. Ladder2

import sys

sys.stdin = open('python/algorithm/swea/D4/input.txt')

# dy = [0, 0]
dx = [-1, 1]  # 좌, 우 이동

for _ in range(1, 11):
    tc = int(input())
    start_list = []
    ladder = []

    for i in range(100):  # 이차원 리스트 만드는 작업
        row = list(map(int, input().split()))
        if i == 0:  # 첫 번째 행을
            for j in range(100):  # 순환하였을 때
                if row[j] == 1:  # 1을 만나면
                    start_list.append(j)  # 시작점 리스트에 저장
        ladder.append(row)

    minimum = {"idx": -1, "step": 10000}  # idx: x좌표, step: 이동 거리
    for x in start_list:  # 시작점 순환
        start_point = x  # 시작점 미리 저장
        step = 1  # 이동거리 측정
        # visited = [[False] * 100 for _ in range(100)]
        y = 0  # 열 변수

        while y < 99:  # 마지막 줄에 다다르면 반복문 종료
            # visited[y][x] = True
            for d in range(2):  # 좌우 탐색
                if (
                    0 <= x + dx[d] < 100  # 가보려는 곳이 유효성 검사를 충족하면서
                    # and not visited[y][x + dx[d]]
                    and ladder[y][x + dx[d]] == 1  # 연결된 곳일 경우
                ):
                    while ladder[y + 1][x + dx[d]] == 0:  # 가려는 곳의 바로 밑칸이 0이라면
                        # visited[y][x + dx[d] * i] = True
                        step += 1  # 이동거리 + 1과
                        x += dx[d]  # 좌/우 한칸 이동을 반복한다.

                    step += 1  # 가려는 곳의 바로 밑칸이 0이 아니라면
                    x += dx[d]  # 좌/우 한칸 이동한 후
                    break  # 방향에 대한 반복문을 종료한다.

            y += 1  # 좌/우의 길 존재 여부에 관계없이
            step += 1  # 한칸 밑으로 내려간다.

        if step <= minimum["step"]:  # 현재 x좌표일 때의 이동거리와 저장된 최소 이동 거리를 비교
            minimum["step"] = step
            minimum["idx"] = start_point

    print(f"#{tc} {minimum['idx']}")

# 숫자 배열 회전

for tc in range(1, int(input()) + 1):
    print(f'#{tc}')

    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]  # 숫자를 각각 뗀 리스트로 받음

    # 90도 회전
    first = list(zip(*board[::-1]))  # 90도의 경우, 해당 값을 거꾸로 돌려서 해당 값을 세로를 가로로 묶어줌

    # 180도 회전
    second = board[::-1]  # 우선, board값을 거꾸로 돌림
    for i in range(n):  # 거꾸로 돌린 값에 대하여 한 줄씩 거꾸로 저장
        second[i] = second[i][::-1]

    # 270도 회전
    third = first[::-1]  # 90도 회전한 값을 거꾸로 돌림
    for j in range(n):  # 행마다 거꾸로 저장
        third[j] = third[j][::-1]

    for k in range(n):
        print(*first[k], sep='', end=' ')
        print(*second[k], sep='', end=' ')
        print(*third[k], sep='', end=' ')
        print()

# 가랏! RC카!

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    now_v = 0
    distance = 0
    command = [list(map(int, input().split())) for _ in range(N)]

    for per_second in command:
        if per_second[0] == 1:
            now_v += per_second[1]
        elif per_second[0] == 2:
            now_v -= per_second[1]
        if now_v < 0:
            now_v = 0
        distance += now_v

    print(f'#{test_case} {distance}')




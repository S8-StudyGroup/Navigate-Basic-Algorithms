# 가랏! RC카!

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    vel_now = 0  # 현재 속도
    dis = 0  # 이동거리

    for sec in range(1, N + 1):
        # 1. input() 개수가 다름 -- 리스트로 받기
        command_list = list(map(int, input().split()))

        if command_list[0] == 1:  # 가속(1)
            vel_now += command_list[1]

        elif command_list[0] == 2:  # 감속(2)
            if vel_now < command_list[1]:  # 현재 속도보다 감속할 속도가 더 클 경우
                vel_now == 0
            else:
                vel_now -= command_list[1]

        else:  # 속도 유지(0)
            vel_now

        dis += vel_now

    print(f'#{test_case} {dis}')

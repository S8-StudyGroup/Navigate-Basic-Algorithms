# 가랏! RC카!

# 총 테스트 케이스의 개수
T = int(input())

for test_case in range(1, T + 1):

    # 속도, 이동거리
    speed = 0
    distance = 0

    # Command의 수
    N = int(input())

    for time in range(1, N + 1):

        # Command 저장
        command = list(map(int, input().split()))

        # 가속 및 감속 케이스
        if command[0] == 1:
            speed += command[1]
        elif command[0] == 2:
            speed -= command[1]

            # 감속할 속도가 더 큰 경우, 속도를 0m/s로 설정
            if speed < 0:
                speed = 0

        # 이동거리 계산
        distance += speed

    # 이동거리 출력
    print(f'#{test_case} {distance}')

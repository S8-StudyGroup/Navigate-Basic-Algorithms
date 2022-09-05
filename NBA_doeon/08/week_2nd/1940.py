# 가랏! RC카!

T = int(input())

for test_case in range(1, T + 1):

    # 1. 각 test_case의 mode, a 리스트를 완성하기
    mode = [0]  # 각 step의 주행모드(0 or 1 or 2)으로 이뤄진 리스트
    a = [0]  # 각 step의 가속도로 이뤄진 리스트

    for i in range(int(input())):  # 주어진 step 개수마다 for문
        list_line = input().split()  # 한 input 줄에 mode와 a가 섞여있기 때문에 각 줄을 split한 다음

        # 밑 if,else 구문이 필요한 이유 : 0인 경우에는 m, v로 input 값이 저장하고자 하는 곳과 개수가 맞지 않아 Error 발생
        # 만약 주행모드가 0이 아닌 경우
        if len(list_line) == 2:  ## -> 각 주행모드와 가속도를 리스트에 삽입
            m, v = map(int, list_line)
            mode.append(m)
            a.append(v)
        
        # 만약 주행모드가 0인 경우
        else:  ## -> 주행모드와 가속도는 모두 0으로 리스트에 삽입
            mode.append(0)
            a.append(0)

    # 2. test_case의 속도 velocity 리스트 완성하기
    ## 주의사항 : 속도는 모드에 따라, 현재 step의 전 step의 속도에 영향을 받기 때문에 위의 mode, a와 별개의 리스트 생성해줌

    velocity = [0]  # 처음 index에 0을 넣는 이유 : velocity 구할 때 처음 속도가 계산식에 포함되기 때문

    # 주행모드에 따라 velocity의 계산이 달라지므로 if, elif,f else로 나눔
    for status in range(1, len(mode)):

        # 주행모드 1) 이전 velocity에 현재 가속도 더한 값
        if mode[status] == 1:
            velocity.append(velocity[status - 1] + a[status])

        # 주행모드 2) 이전 velocity에 현재 가속도를 뺀 값, 결과가 음수면 속도는 0
        elif mode[status] == 2:
            if velocity[status - 1] - a[status] <= 0:
                velocity.append(0)
            else:
                velocity.append(velocity[status - 1] - a[status])

        # 주행모드 0) 이전 velocity 그대로
        else:
            velocity.append(velocity[status - 1])

    # 3. distance = velocity * t에서 t는 항상 1임으로 distance는 그냥 velocity 리스트 요소를 모두 더한 값
    print(f'#{test_case} {sum(velocity)}')

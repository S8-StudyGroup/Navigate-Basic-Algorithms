# 4013. 특이한 자석

t = int(input())
k = int(input())

for tc in range(1, t + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    turn = [list(map(int, input().split())) for _ in range(k)]

    print(arr)
    print(turn)

    # 일단 제일 먼저 뭘 해야 하냐면 뭘 돌릴 건지 정해야지 그건 turn 리스트에 있음

    for i in range(len(turn)):
        gear = turn[i][0] # 얘가 돌릴 주체 기어 번호가 나옴
        direction = turn[i][1] # 돌릴 방향 나옴 1 또는 -1

        # 돌릴 애 정했으면 이제 뭘 봐야해? 돌릴 애의 2,6번째 인덱스랑 그 옆의 톱니바퀴의 6,2 인덱스
        # 체크했을 때, 둘이 다르면, direction과 반대로 해당 arr를 돌린다

        # 해당 기어의 2번째랑 그 오른쪽 기어의 6번째가 다르면?
        if 0 <= gear - 1 + 1 < 8 and arr[gear - 1][2] != arr[gear - 1 + 1][6]:
            # 해당 기어도 돌리고, 오른쪽 애는 반대로 돌리자
            if direction == 1:
                arr[gear - 1].insert(0, arr[gear - 1].pop())
                arr[gear - 1 + 1].insert(7, arr[gear - 1 + 1].pop(0))

            elif direction == -1:
                arr[gear - 1].insert(7, arr[gear - 1].pop(0))
                arr[gear - 1 + 1].insert(0, arr[gear - 1 + 1].pop())


        # 해당 기어의 6번째랑 그 왼쪽의 기어의 2번째가 다르면?
        elif 0 <= gear - 1 - 1 < 8 and arr[gear - 1][6] != arr[gear - 1 - 1][2]:
            # 해당 기어도 돌리고, 오른쪽 애는 반대로 돌리자
            if direction == 1:
                arr[gear - 1].insert(0, arr[gear - 1].pop())
                arr[gear - 1 + 1].insert(7, arr[gear - 1 + 1].pop(0))

            elif direction == -1:
                arr[gear - 1].insert(7, arr[gear - 1].pop(0))
                arr[gear - 1 + 1].insert(0, arr[gear - 1 + 1].pop())

    print(arr)

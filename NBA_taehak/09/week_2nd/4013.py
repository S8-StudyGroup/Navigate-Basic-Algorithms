# 4013. 특이한 자석

# 3. 명령을 수행하는 함수
# DFS와 유사하게
edges = [[], [2], [1, 3], [2, 4], [3]]


def go(command):
    gear_num, direction = command

    if direction == 0:
        return

    output[gear_num] = direction

    # 주변 탐색
    for edge in edges[gear_num]:

        # 방문처리 안된곳 (원래 자리로 돌아오는 것을 방지하기 위한 조건)
        if output[edge] == 0:

            # 왼쪽 톱니
            if edge < gear_num:
                # 자성이 다르면 회전 진행 계획 저장
                if gear[edge][2] != gear[gear_num][-2]:
                    output[edge] = direction * -1

            # 오른쪽 톱니
            else:
                if gear[edge][-2] != gear[gear_num][2]:
                    output[edge] = direction * -1

            go((edge, output[edge]))

    return


# 4.0. 회전시켜주는 함수
def rotate(gear, direction):
    if direction == 0:
        return

    if direction == 1:
        a = gear.pop()
        gear.insert(0, a)
    else:
        a = gear.pop(0)
        gear.append(a)


for case in range(1, int(input()) + 1):
    k = int(input())

    # 1. 나중에 번호로 톱니 정보를 불러와야 하니까 그거 생각해서 자료구조 생성
    gear = dict()
    for i in range(1, 5):
        gear[i] = list(map(int, input().split()))

    # 2. 회전 명령
    commands = [list(map(int, input().split())) for _ in range(k)]

    # 4. 명령 실행
    for command in commands:
        output = [0] * 5
        go(command)
        for gear_num in range(1, 5):
            rotate(gear[gear_num], output[gear_num])

    # 5. 점수 계산
    score = 0
    for idx, gear in enumerate(gear.values()):
        score += gear[0] * (2**idx)

    print(f'#{case} {score}')

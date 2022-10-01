# 1220. Magnetic
import sys

sys.stdin = open("input.txt")

t = 10

for tc in range(1, t + 1):
    n = int(input())
    arr = [list((map(int, input().split()))) for _ in range(n)]

    # 1 N극 성질을 가지는 자성체 2. S극 성질을 가지는 자성체
    count = 0
    for j in range(n):  # 이차원 리스트를 활용
        move = 0        # 마지막으로 확인한 자성체 종류 저장시킬 변수
        for i in range(n):
            if arr[i][j] != 0:      # 자성체인지 아닌지 확인
                if arr[i][j] == 2:  # S극이라면
                    if move == 1:   # 마지막 확인한 자성체가 N극이면
                        count += 1  # 교착상태 수 + 1
                move = arr[i][j]    # 마지막 자성체 바꿔준다
    print(f'#{tc} {count}')
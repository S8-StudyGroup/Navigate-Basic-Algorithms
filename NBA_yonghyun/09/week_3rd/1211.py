# [SWEA] 1211. Ladder2
'''
아이디어

1. 어느 사다리가 최단거리?
2. ladder[0][i] == 1 일 때만 최단거리 계산 코드 진행
3. 좌우 델타 확인 // 없으면 아래로
4. 같은 방향으로 계속 이동 (가능할 때까지)
5. 좌우 중 한 방향으로 이동했으면, 반대 방향으로는 이동 X
6. 최단거리를 가지는 시작점 (인덱스) 필요

'''

delta = [-1, 1]  # 좌, 우

for _ in range(10):
    t = int(input())  # 테스트 케이스 번호
    ladder = [list(map(int, input().split())) for _ in range(100)]
    min_move = 100 * 100  # 최소 이동거리 기본값
    min_idx = -1  # 최소 이동 시작점

    for i in range(100):
        x = i  # x좌표 (가로 이동)
        y = 1  # y좌표 (세로 이동)
        move = 0

        # 2. 출발점이 0이면 고려 X
        if ladder[0][i] == 0:
            pass
        else:
            while y <= 99:
                end = False

                # 3. 좌우 델타 확인 // 없으면 아래로 (else 문)
                for d in delta:
                    # 5. 좌우 중 한 방향으로 이동했으면, 반대 방향으로는 이동 X
                    if end:  # 델타이동 for 문을 멈추는 종료조건
                        y += 1
                        move += 1
                        break

                    # 4. 범위 내 + 값이 1인 칸이면 계속 이동
                    while 0 <= x + d <= 99:
                        if ladder[y][x + d] == 1:
                            x = x + d
                            move += 1
                            end = True  # 좌우 중 한쪽 방향으로 이동을 했기 때문에, 반대로는 가지 않겠다
                        else:
                            break
                else:
                    y += 1
                    move += 1

            if min_move > move > 0:  # 사다리가 없는 곳은 move 값이 0이므로, 최단거리는 0보다 커야 함
                min_move = move
                min_idx = i  # 6. 최단거리를 가지는 시작점

    print(f'#{t} {min_idx}')

'''
if - else 문
조건 바꿔서 -> pass 안 해도 됨!
'''

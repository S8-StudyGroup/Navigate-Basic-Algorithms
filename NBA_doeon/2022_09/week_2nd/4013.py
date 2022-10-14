# 4013. 특이한 자석


def find_target(target_m, dir):
    visited[target_m] = True
    left = target_m - 1
    right = target_m + 1

    if 1 <= left <= 4 and not visited[left]:
        if mag[target_m][6] != mag[left][2]:  # 타겟의 왼쪽
            will_be_turned.append((left, -dir))
            find_target(left, -dir)
    if 1 <= right <= 4 and not visited[right]:
        if mag[target_m][2] != mag[right][6]:  # 타겟의 오른쪽
            will_be_turned.append((right, -dir))
            find_target(right, -dir)


t = int(input())
for tc in range(1, t + 1):
    k = int(input())

    mag = [list(map(int, input().split())) for _ in range(4)]
    mag = [0] + mag
    plays = [list(map(int, input().split())) for _ in range(k)]
    score = [0, (0, 1), (0, 2), (0, 4), (0, 8)]

    # print(mag)

    for play in plays:
        start_m = play[0]
        d = play[1]

        will_be_turned = [(start_m, d)]
        visited = [True] + [False] * 4
        # print(visited)
        find_target(start_m, d)

        # 그럼 이제 나온 wbt으로 자석들 리스트 pop해서 한칸씩 이동해주자
        for turn in will_be_turned:
            mag_num, turn_dir = turn

            if turn_dir == 1:
                last = mag[mag_num].pop()
                mag[mag_num] = [last] + mag[mag_num]
            elif turn_dir == -1:
                first = mag[mag_num].pop(0)
                mag[mag_num] = mag[mag_num] + [first]

    # 이제 돌리기 게임 끝! 점수 합산할 시간
    score_cnt = 0
    # print(len(mag))
    for idx in range(1, len(mag)):
        position = mag[idx][0]
        score_cnt += score[idx][position]

    print(f'#{tc} {score_cnt}')

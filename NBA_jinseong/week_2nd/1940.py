# 가랏! RC카!

for t in range(1, int(input()) + 1):
    rc_state = 0
    distance = 0
    for n in range(1, int(input()) + 1):
        li = list(map(int, input().split()))
        if 0 < li[0] <= 2:
            rc_change, acc = li[0:2]
        elif li[0] == 0:
            rc_change = li[0]
        else:
            continue

        if rc_change == 0:
            distance += rc_state
        elif rc_change == 1:
            rc_state += acc
            distance += rc_state
        elif rc_change == 2:
            if rc_state > acc:
                rc_state -= acc
                distance += rc_state
            else:  # 감속값이 현 속도값보다 작으면
                rc_state = 0
        else:
            pass

    print(f'#{t} {distance}')

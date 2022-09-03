# 날짜 계산기

'''
[ 아이디어 ]


마지막 날짜에 따라 달 나누기 (28일, 30일, 31일)

주어진 두개의 날짜가
1. 같은 달일 때
 -> 일의 차만 구하면 됨 (+1)
2. 다른 달일 때
 -> 일의 차 + 달의 차 (* 해당 달의 일)
    - 달의 차만큼 for문
    - if문 : 중간에 껴있는 달들이 몇일인지

'''


t = int(input())

d_28 = [2]
d_30 = [4, 6, 9, 11]
d_31 = [1, 3, 5, 7, 8, 10, 12]

for test_case in range(1, t + 1):
    sm, sd, em, ed = map(int, input().split())

    dif = 0

    # 같은 달일 때
    if sm == em:
        dif = ed - sd + 1  # 시작날까지 포함하기 위해 +1 해줌

    # 다른 달일 때
    else:
        # 첫 번째 달부터 두 번째 달까지
        for m in range(sm, em):

            # 해당 달이 28일일 때
            if m in d_28:
                dif += 28

            # 해당 달이 30일일 때
            elif m in d_30:
                dif += 30

            # 해당 달이 31일일 때
            else:
                dif += 31

        # 일의 차만큼을 더해줌
        else:
            dif += ed - sd + 1  # 시작날까지 포함하기 위해 +1 해줌

    print(f'#{test_case} {dif}')

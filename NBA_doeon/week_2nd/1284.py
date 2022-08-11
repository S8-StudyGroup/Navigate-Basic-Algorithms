# 수도 요금 경쟁

T = int(input())

for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())

    A_fee = P * W

    if W < R:
        B_fee = Q
    else:
        B_fee = Q + (W - R) * S

    print(f'#{test_case} {A_fee if A_fee < B_fee else B_fee}')

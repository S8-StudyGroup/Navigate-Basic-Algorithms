# 수도 요금 경쟁

T = int(input())

for test_case in range(1, 1 + T):
    P, Q, R, S, W = map(int, input().split())

    A_money = W * P
    if W <= R:
        B_money = Q
    else:
        B_money = Q + (W - R) * S

    print(f'#{test_case} {min(A_money, B_money)}')

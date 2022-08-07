# 수도 요금 경쟁

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    
    A_fee = P * W
    
    if W < R:
        B_fee = Q
    else:
        B_fee = Q + (W - R) * S
        
    print(f'#{test_case} {A_fee if A_fee < B_fee else B_fee}')

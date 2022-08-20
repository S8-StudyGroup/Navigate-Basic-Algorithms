# 수도 요금 경쟁

# 테스트 케이스의 개수 저장
T = int(input())

# 각 테스트 케이스
for test_case in range(1, T + 1):

    # P, Q, R, S, W 값 저장
    P, Q, R, S, W = map(int, input().split())
    ans = 0

    # A, B사 요금 계산
    # 월간 사용량 W이 R리터 이하일 경우 기본 요금만 청구
    # R리터보다 많을 경우 **초과량**에 대해 1리터랑 S원의 요금 청구
    costA = W * P
    costB = 0
    if W <= R:
        costB = Q
    else:
        costB = Q + (W - R) * S

    # 더 저렴한 요금 출력
    if costA < costB:
        ans = costA
    else:
        ans = costB
    print(f"#{test_case} {ans}")

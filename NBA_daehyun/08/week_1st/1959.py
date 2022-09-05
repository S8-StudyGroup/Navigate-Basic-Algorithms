# 두 개의 숫자열
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    repeat_num = abs(N - M) + 1
    if N >= M:
        for i in range(repeat_num):
            inner_product = 0
            for j in range(M):
                inner_product += B[j] * A[j + i]
            C.append(inner_product)
    else:
        for i in range(repeat_num):
            inner_product = 0
            for j in range(N):
                inner_product += A[j] * B[j + i]
            C.append(inner_product)
    print(f'#{test_case} {max(C)}')

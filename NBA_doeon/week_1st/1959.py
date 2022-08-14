# 두 개의 숫자열

T = int(input())
for test_case in range(1, T + 1):

    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if len(A) > len(B):
        L = A[:]
        S = B[:]
    else:
        L = B[:]
        S = A[:]

    # if len(A) < len(B):
    #     A, B = B, A

    num = []

    for i in range((len(L) - len(S) + 1)):
        sum = 0
        for j in range(len(S)):
            sum += S[j] * L[i + j]
        num.append(sum)

    answer = max(num)
    print(f'#{test_case} {answer}')
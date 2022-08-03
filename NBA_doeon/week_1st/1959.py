# 두 개의 숫자열

T = int(input())
for test_case in range(1, T + 1):
    
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    num = []
    
    for i in range((len(B) - len(A) + 1)):
        sum = 0
        for j in range(len(A)):
            sum += (A[j] * B[i + j])
        num.append(sum)
        
    answer = max(num)
    print(f'#{test_case} {answer}')
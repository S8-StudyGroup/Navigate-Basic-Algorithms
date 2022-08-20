# 간단한 소인수분해

def func(divider, N):
    count = 0
    while N % divider == 0:
        N /= divider
        count += 1
    return count


for test_case in range(1, int(input()) + 1):
    N = int(input())
    print(f'#{test_case} {func(2, N)} {func(3, N)} {func(5, N)} {func(7, N)} {func(11, N)}')


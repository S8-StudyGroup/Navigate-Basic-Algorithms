# 간단한 N의 약수

N = int(input())
print(*[i for i in range(1, N + 1) if N % i == 0])

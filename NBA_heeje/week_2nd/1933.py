# 간단한 N 의 약수

# 1개의 정수 N 입력 받음
N = int(input())

ans_list = [i for i in range(1, N + 1) if N % i == 0]

print(*ans_list)

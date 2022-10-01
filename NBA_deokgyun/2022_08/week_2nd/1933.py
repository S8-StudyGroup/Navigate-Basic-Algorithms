# 간단한 N의 약수

N = int(input())

result_list = []

for i in range(1, N + 1):
    if N % i == 0:
        result_list.append(i)

print(*result_list)

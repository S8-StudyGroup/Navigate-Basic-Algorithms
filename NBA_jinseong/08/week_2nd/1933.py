# 간단한 N의 약수
n = int(input())

measure = []

for i in range(1, n + 1):
    if n % i == 0:
        measure.append(i)

print(*measure)

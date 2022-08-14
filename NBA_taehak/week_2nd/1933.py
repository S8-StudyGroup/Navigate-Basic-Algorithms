# 간단한 N의 약수

n = int(input())
di = []

for i in range(1, n + 1):
    if n % i == 0:
        di.append(i)

print(*di)

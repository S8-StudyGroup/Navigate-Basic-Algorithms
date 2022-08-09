# 간단한 N의 약수

num = int(input())

for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=' ')

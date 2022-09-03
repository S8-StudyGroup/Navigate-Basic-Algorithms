# 간단한 N의 약수


## 첫번째 코드

N = int(input())

index = 1

while index <= N:
    if N % index == 0:
        print(index, end=' ')
    index += 1


## 두번째 코드

N = int(input())

for i in range(1, N + 1):
    if N % i == 0:
        print(i, end=' ')

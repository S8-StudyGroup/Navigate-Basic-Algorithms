# 간단한 N의 약수

N = int(input())

data = ['1']

for i in range(2, N +1):
    if N % i == 0:
        data.append(str(i))


print(' '.join(data))
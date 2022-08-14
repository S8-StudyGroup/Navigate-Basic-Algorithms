# 아주 간단한 계산기

def calculator(x, y):
    return x + y, x - y, x * y, x // y


a, b = map(int, input().split())

for i in range(4):
    print(calculator(a, b)[i])

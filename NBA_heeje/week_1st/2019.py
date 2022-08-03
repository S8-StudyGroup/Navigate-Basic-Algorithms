# 더블더블

# N 입력 받아 저장
N = int(input())
c = 0
while c <= N:
    print(2**c, end=" ")
    c += 1

# 간단하게

# print(*[2 ** i for i in range(int(input()) + 1)])

# 거꾸로 출력해 보아요

# N 입력 받아 저장
N = int(input())

# 언패킹 연산자 이용
print(*[i for i in range(N, -1, -1)])

# 한 줄 답안
# print(*[i for i in range(int(input()), -1, -1)])

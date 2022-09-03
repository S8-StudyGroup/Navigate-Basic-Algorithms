# N줄덧셈
T = int(input())
print(T * (T + 1) // 2)

# 1. 등차수열의 합 공식
# 시간복잡도 : O(4) = O(1)
# sum = N * (N + 1) // 2


# 2. 1부터 N까지 반복문을 돌며 합을 계산
# 시간복잡도 : O(N)
# sum = 0
# for i in range(1, N + 1):
#     sum += i

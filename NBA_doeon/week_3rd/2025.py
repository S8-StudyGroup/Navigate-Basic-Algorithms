# N줄덧셈

num = int(input())
result = 0

# 0부터 입력값 정수까지 반복문을 돌면서 덧셈
for i in range(1, num + 1):
    result += i

print(result)

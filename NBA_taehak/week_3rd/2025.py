# N줄덧셈

n = int(input())

# 방법 1
print(int(n * (n + 1) / 2))

# 방법 2
result = 0
for i in range(1, n + 1):
    result += i

print(result)

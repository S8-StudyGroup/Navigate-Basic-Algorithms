# 서랍의 비밀번호
target, start = map(int, input().split())

result = target - start
if result < 0:
    result *= -1

print(result + 1)

# [SWEA] 수 이어가기
# Guest - 이가은

n = int(input())

result = [n]

for n2 in range(n, 0, -1):
    numbers = [n, n2]
    # numbers.append(n2)
    n1 = n
    for _ in range(n + 1):
        # while True:
        n3 = n1 - n2
        if n3 >= 0:
            numbers.append(n3)
        else:
            break
        n1 = n2
        n2 = n3

    if len(numbers) > len(result):
        result = numbers

print(len(result))
print(*result)

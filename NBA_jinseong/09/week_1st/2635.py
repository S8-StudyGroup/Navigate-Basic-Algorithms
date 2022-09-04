# 2635. 수 이어가기


def rule(number, start):
    global result_cnt, result_numbers

    if number - start >= 0:
        numbers.append(number - start)
        result_cnt += 1
        rule(numbers[-2], numbers[-1])
    else:
        result_numbers.append(numbers)


n = int(input())

result_cnt = []
result_numbers = []

for i in range(1, n+1):
    cnt = 2
    numbers = [n, i]
    rule(n, i)

m = max(result_cnt)
for v in result_numbers:
    if len(v) == m:
        print(m)
        print(*v)
        break

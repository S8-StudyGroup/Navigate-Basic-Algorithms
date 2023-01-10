# [BOJ] 9020. 골드바흐의 추측

memo = set()

for num in range(2, 10001):
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            break
    else:
        memo.add(num)

T = int(input())

for _ in range(T):
    n = int(input())
    for a in range(n // 2, 1, -1):
        if a in memo and n - a in memo:
            print(a, n - a)
            break


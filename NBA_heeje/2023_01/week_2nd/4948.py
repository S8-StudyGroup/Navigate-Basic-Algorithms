# [BOJ] 4948. 베르트랑 공준

prime_set = set()
numbers = list(range(2, 246913))
for n in numbers:
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            break
    else:
        prime_set.add(n)

while True:
    n = int(input())
    
    if n == 0:
        break

    ans = 0

    for num in range(n + 1, 2 * n + 1):
        if num in prime_set:
            ans += 1
    
    print(ans)

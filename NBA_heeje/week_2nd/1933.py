# 간단한 N 의 약수


# Case 1
# 시간 복잡도 O(N)
# 약 10억까지 가능
def case_1(num):
    return [i for i in range(1, num + 1) if num % i == 0]


# Case 2
# 해당 숫자의 제곱근까지만 반복문을 돌려도 모든 약수를 구할 수 있다.
# 시간 복잡도 O(N^(1/2))
# 약 10억의 제곱까지 가능
def case_2(num):
    divisors = []
    for i in range(1, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            divisors.append(i)
            if num // i != i:
                divisors.append(num // i)

    return sorted(divisors)


N = int(input())  # N = 100일 때

print(*case_1(N))  # 1 2 4 5 10 20 25 50 100
print(*case_2(N))  # 1 2 4 5 10 20 25 50 100

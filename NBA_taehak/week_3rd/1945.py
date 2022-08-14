# 간단한 소인수분해
def facto(num, prime_num):
    '''
    num : 숫자 입력
    prime_num : 소인수
    return : 소인수로 몇번 나뉘는지
    '''
    count = 0
    while num % prime_num == 0:
        num //= prime_num
        count += 1
    return count, num


cases = int(input())
prime_numbers = [2, 3, 5, 7, 11]

for case in range(1, cases + 1):
    number = int(input())
    factorization = []

    for prime_number in prime_numbers:
        count, number = facto(number, prime_number)
        factorization.append(count)

    print(f'#{case}', *factorization)

# 몫과 나머지 출력하기

for test_case in range(1, int(input()) + 1):
    n1, n2 = map(int, input().split())
    print(f'#{test_case} {n1 // n2} {n1 % n2}')
# 몫과 나머지 출력하기

for t in range(1, int(input()) + 1):
    a, b = map(int, input().split())

    share = a // b
    remainder = a % b

    print(f'#{t} {share} {remainder}')


# 몫과 나머지 출력하기

for case in range(1, int(input()) + 1):
    a, b = map(int, input().split())
    print(f'#{case} {a//b} {a%b}')

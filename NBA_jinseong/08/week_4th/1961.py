# 숫자 배열 회전

for t in range(1, int(input()) + 1):
    n = int(input())

    li = [list(map(int, input().split())) for _ in range(n)]

    print(f'#{t}')
    for i in range(n):
        for j in range(n):
            print(li[n-1-j][i], end='')
        print(end=' ')
        for j in range(n):
            print(li[n-1-i][n-1-j], end='')
        print(end=' ')
        for j in range(n):
            print(li[j][n-1-i], end='')
        print()


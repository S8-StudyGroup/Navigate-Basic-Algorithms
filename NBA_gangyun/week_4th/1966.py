# 숫자를 정렬하자

for t in range(1, int(input()) + 1):
    N = int(input())
    print(f'#{t}', *sorted(list(map(int, input().split()))))

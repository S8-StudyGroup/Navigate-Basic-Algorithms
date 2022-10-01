# 숫자를 정렬하자

for t in range(1, int(input()) + 1):
    n = int(input())
    numbers = list(map(int, input().split()))

    print(f'#{t}', *sorted(numbers))
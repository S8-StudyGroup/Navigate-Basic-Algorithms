# 간단한 압축풀기

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    words = ''

    print()
    print(f'#{tc}')
    
    for i in range(n):
        letter, number = input().split()
        words += letter * int(number)

    for j in range(1, len(words) + 1):
        if j % 10 == 0:
            print(words[j - 1])
        else:
            print(words[j - 1], end='')
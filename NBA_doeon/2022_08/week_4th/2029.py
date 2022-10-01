# 몫과 나머지 출력하기

t = int(input())

for tc in range(1, t + 1):
    a, b = map(int, input().split())
    
    i = a // b
    j = a % b
    
    print(f'#{tc} {i} {j}')
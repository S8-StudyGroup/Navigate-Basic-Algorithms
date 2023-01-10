# [BOJ] 10815. 숫자 카드

n = int(input())
my = set(map(int, input().split()))
m = int(input())
compare = list(map(int, input().split()))
result = []

for idx in range(m):        
    subject = compare[idx]  # 가진 숫자카드와 비교할 숫자 대상
    
    if subject in my:       # set의 in 연산 -> O(1)
        result.append(1)
    else:
        result.append(0)

print(*result)
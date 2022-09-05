# 간단한 소인수분해

t = int(input())
# n : 소인수 리스트
n = [2, 3, 5, 7, 11]

for tc in range(1, t + 1):
    # number : 입력값
    number = int(input())
    # divide_cnts : 나머지가 0으로 나누어진 횟수로 이뤄진 리스트
    divide_cnts = [0] * len(n)

    for i in range(len(n)):
        # divide_cnt : 각 소인수(i)로 나눴을 때 횟수
        divide_cnt = 0
        
        # number가 소인수 리스트의 특정 소인수 i로 나눴을 때 나머지가 0일 때까지
        while number % n[i] == 0:
            divide_cnt += 1 # 횟수를 한 번 더함
            number = number / n[i] # 횟수 더한 후 number는 나눠진 수로 업데이트
        
        divide_cnts[i] = divide_cnt

    print(f'#{tc}', end=' ')
    print(*divide_cnts) # 참고 : f-string 쓸 때에 {}안에서는 * 쓸 수 없음!
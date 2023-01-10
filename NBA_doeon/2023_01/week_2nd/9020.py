# [BOJ] 9020. 골드바흐의 추측

def check(s):               # 소수인지 체크하는 함수 check
    for d in range(2, s):   # 나눌 수 d는 2부터 (체크할 숫자-1)까지
        if s % d == 0:      # 나눠지면 소수 x
            return 0
    else:                   # 위의 if문에 한 번도 안 걸렸다면 소수 O
        return 1


t = int(input())        # 테케 개수

for tc in range(t):
    n = int(input())    # 대상 숫자 n

    num1 = int(n / 2)   # n의 절반 값 num1
    num2 = n - num1     # n과 num1의 차이 num2

    while True:         # 정답을 찾을 때까지 반복해야 한다.

        if check(num1) + check(num2) == 2:  # 만약 num1, num2 둘 다 소수면
            print(num1, num2)               # 두 숫자를 출력하고 현재 테케를 중단한다
            break

        else:                               # 아니면 다음 짝으로 넘어가야 한다
            num1 -= 1                       # num1은 하나 줄이고, num2는 하나 늘리면서 반복
            num2 += 1
            continue
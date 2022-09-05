# 간단한 소인수분해
import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    number = int(input())
    num = [2, 3, 5, 7, 11]
    # 소인수 리스틀 만들어줌
    result = [0] * len(num)
    # 횟수를 담을 리스트를 생성
    for i in range(len(num)):
        while True:
            if number % num[i] == 0:
                # 만약 number를 num의 i번째 숫자로 나눈 나머지가 0이라면
                number = number//num[i]
                # number를 그 몫으로 바꾸고
                result[i] += 1
                # result에 하나 카운트 해준다. 
            else:
                break
                # 만약 나머지가 0이 아니라면 num의 다음 i로 넘어감
    print(f"#{tc}", *result)
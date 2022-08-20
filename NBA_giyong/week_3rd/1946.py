# 간단한 압축풀기
import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    answer = ''
    for i in range(n):      # 저장할 자료가 많아 반복문으로 받아준다.
        data = input().split()
        answer += data[0] * int(data[1])     # 둘다 문자열로 받아줬음으로 두번째 data를 숫자로 변환시켜준다. 

    print(f"#{tc}")
    for i in range(0, len(answer), 10):     # 너비가 10이 넘어가면 안되니까 줄바꿈을 해준다.
        if len(answer) > 10:
            print(answer[i:i+10], end='\n')
        else:
            print(answer[i:i+10])
            
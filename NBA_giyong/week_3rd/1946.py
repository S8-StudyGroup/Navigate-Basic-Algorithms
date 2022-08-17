# 간단한 압축풀기
import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    answer = ''
    for i in range(n):
        data = input().split()
        answer += data[0] * int(data[1])

    print(f"#{tc}")
    for i in range(0, len(answer), 10):
        if len(answer) > 10:
            print(answer[i:i+10], end='\n')
        else:
            print(answer[i:i+10])
            
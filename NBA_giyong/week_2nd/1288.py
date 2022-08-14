# 새로운 불면증 치료법
import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    n = input()
    value = int(n)
    data = [0]*10 
    while True:
        for i in range(len(n)):
            data[int(n[i])] += 1
        if not data.count(0):  
            print(f"#{tc} {int(n)}")
            break   
        n = str(value + int(n))
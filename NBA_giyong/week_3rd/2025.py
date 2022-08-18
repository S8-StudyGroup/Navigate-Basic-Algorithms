# N줄덧셈
import sys

sys.stdin = open("input.txt")

number = int(input())

number_sum = 0
for i in range(1, number + 1):
    number_sum += i

print(number_sum)
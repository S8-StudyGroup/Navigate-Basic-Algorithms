# 더블더블
num = int(input())

result = 1
for n in range(num):  # num 수 만큼 * 2
    print(result, end=' ')
    result *= 2
print(result)  # 마지막 * 2 후 for문을 나오므로 마지막숫자 출력

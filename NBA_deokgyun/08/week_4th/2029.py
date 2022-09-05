# 몫과 나머지 출력하기
for test_count in range(1, int(input()) + 1):
    a, b = map(int, input().split())
    print(f"#{test_count}", a // b, a % b)

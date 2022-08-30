# 시각 덧셈

t = int(input())

for test_case in range(1, t + 1):
    h1, m1, h2, m2 = map(int, input().split())

    # 분부터 처리
    h3 = 0
    m = m1 + m2
    if m1 + m2 >= 60:
        h3 = 1
        m = m - 60

    # 시 처리
    h = h1 + h2 + h3
    if h > 12:
        h = h - 12

    print(f'#{test_case} {h} {m}')


'''
12:30 + 12:40 했을 때,
왜 통과했지..?

-> while h > 12:
        h = h - 12

또는 몫과 나머지
'''

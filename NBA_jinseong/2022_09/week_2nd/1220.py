# 1220. Magnetic

for t in range(1, 11):
    n = int(input())

    # 어차피 나중에 str 타입으로 데이터를 처리할거라 int mapping 안함
    table = [input().split() for _ in range(n)]

    cnt = 0

    for j in range(n):
        line = ''
        for i in range(n):
            line = line + table[i][j]
        # 사이사이에 빈공간인 0을 없애줌
        line = line.replace('0', '')
        # 1다음 2가 오면 교착상태이므로 12의 개수를 셈
        cnt += line.count('12')

    print(f'#{t} {cnt}')

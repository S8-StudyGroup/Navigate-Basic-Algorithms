# [BOJ] 14889. 스타트와 링크

n = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

from itertools import combinations

number = range(n)
half = int(n/2)
min_diff = 10000

for case in combinations(number, half): # 조합으로 발생하는 케이스마다 확인

    a = case    # A팀
    b = []      # B팀
    for rest in range(n):
        if rest not in a:
            b.append(rest)

    diff = 0    # A에서의 조합, B에서의 조합의 값 차이(케이스마다 존재)

    for i in range(half - 1):           # 팀에서 발생할 수 있는 조합
        for j in range(i + 1, half):
            a1 = a[i]                   # i인덱스를 사람1
            a2 = a[j]                   # j인덱스를 사람2로 사람1과 사람2 사이의 발생 능력치 계산
            b1 = b[i]                   # B팀의 경우도 똑같이 진행
            b2 = b[j]

            # 발생하는 조합 케이스마다 매번 능력치 합 차이를 구해서 diff에 반영
            diff += (matrix[a1][a2] + matrix[a2][a1]) - (matrix[b1][b2] + matrix[b2][b1])

    # diff 최소값을 찾기 위해 갱신
    if abs(diff) < min_diff:
        min_diff = abs(diff)

print(min_diff)







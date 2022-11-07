import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
result = 999999
houses = []
bbqs = []

for r in range(n):
    for c in range(n):
        if city[r][c] == 1:
            houses.append([r, c])
        elif city[r][c] == 2:
            bbqs.append([r, c])

for bbq_case in combinations(bbqs, m):
    memo = 0
    for hr, hc in houses:
        bbq_len = 999999
        for br, bc in bbq_case:
            bbq_len = min(bbq_len, abs(hr - br) + abs(hc - bc))
        memo += bbq_len
    result = min(result, memo)

print(result)
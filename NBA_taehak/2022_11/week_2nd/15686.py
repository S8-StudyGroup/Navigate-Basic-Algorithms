import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

houses = []
bbqs = []
for r in range(n):
    for c in range(n):
        if city[r][c] == 1:
            houses.append([r, c])
        elif city[r][c] == 2:
            bbqs.append([r, c])


result = 999999
for bbq_case in combinations(bbqs, m):                              # m개의 치킨집을 고르는 경우의수 마다
    case_memo = 0                                                   # case_memo : 이번 경우의 치킨거리 합
    for hr, hc in houses:                                           # 집마다
        bbq_len = 999999                                            # 치킨거리(최소거리)를 구한다
        for br, bc in bbq_case:                                     # 치킨집마다
            bbq_len = min(bbq_len, abs(hr - br) + abs(hc - bc))     # 거리를 구해서 치킨거리를 구한다.
        case_memo += bbq_len                                        # 해당하는 집의 치킨거리를 case_memo에 더해준다
    result = min(result, case_memo)                                 # 경우의 수마다 치킨거리의 합을 갱신(최소값으로)

print(result)
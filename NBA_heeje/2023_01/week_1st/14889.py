# 스타트와 링크

from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
min_diff = 99999999

for idx, team1 in enumerate(combinations(list(range(N)), N // 2)):      # 1팀의 조합을 구성한 뒤
    team1_set = set(team1)                                              # set으로 변환하여
    team2_set = set(range(N)) - team1_set                               # 전체에서 1팀 멤버를 빼는 방식으로 2팀을 구함
    
    team1_power = 0                                                     # 팀1의 시너지
    team2_power = 0                                                     # 팀2의 시너지

    for i, j in combinations(team1_set, 2):                             # 팀1 내에서 2명씩 조합하여
        team1_power += S[i][j] + S[j][i]                                # 시너지 계산
    
    for i, j in combinations(team2_set, 2):                             # 팀2 내에서 2명씩 조합하여
        team2_power += S[i][j] + S[j][i]                                # 시너지 계산

    diff = abs(team1_power - team2_power)                               # 두 팀의 시너지의 차를 구한 뒤
    if min_diff > diff:                                                 # 최소 차이값 갱신
        min_diff = diff

print(min_diff)
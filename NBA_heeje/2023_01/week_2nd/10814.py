# [BOJ] 10814. 나이순 정렬

import sys
input = sys.stdin.readline

N = int(input())
members = []

for i in range(N):
    members.append(input().split() + [i])

members.sort(key=lambda x: (int(x[0]), x[2]))
members = list(map(lambda x: " ".join(x[:2]), members))

print(*members, sep="\n")

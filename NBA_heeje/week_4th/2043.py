# 서랍의 비밀번호

P, K = map(int, input().split())

if P < K:
    P = P + 1000

print(P - K + 1)

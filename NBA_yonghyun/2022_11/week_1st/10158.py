# [BOJ] 10158. 개미 (실버 4)

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())


nx = t - (w - p)

if (nx // w) % 2 != 0:
    p = nx % w
else:
    p = w - (nx % w)


ny = t - (h - q)

if (ny // h) % 2 != 0:
    q = ny % h
else:
    q = h - (ny % h)


print(p, q)

# 수도 요금 경쟁
t = int(input())

for tc in range(1, t + 1):
    p, q, r, s, w = map(int, input().split())

    a = 0
    b = 0
    if w > r:
        a += p * w
        b += q + (w - r)*s
    else:
        a += p * w
        b += q

    if a < b:
        print(f"#{tc} {a}")
    else:
        print(f"#{tc} {b}")
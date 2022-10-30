# [BOJ] 10158. 개미

w, h = map(int, input().split())
p, q = map(int, input().split())
col_t = row_t = int(input()) % (w * h * 2)

while True:
    if w - p < row_t:
        row_t -= w - p
        p = w
    else:
        p += row_t
        break
    if w < row_t:
        row_t -= p
        p = 0
    else:
        p -= row_t
        break

while True:
    if h - q < col_t:
        col_t -= h - q
        q = h
    else:
        q += col_t
        break
    if h < col_t:
        col_t -= q
        q = 0
    else:
        q -= col_t
        break

print(p, q)
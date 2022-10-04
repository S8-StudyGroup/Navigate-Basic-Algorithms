# boj_7576 토마토

d_r = [0, 0, 1, -1]
d_c = [1, -1, 0, 0]


def change(r, c):
    global row_max, col_max, tomato
    for d in range(4):
        next_r = r + d_r[d]
        next_c = c + d_c[d]

        if 0 <= next_r < row_max and 0 <= next_c < col_max and storage[next_r][next_c] == 0:
            storage[next_r][next_c] = 1
            check.append((next_r, next_c))
            tomato -= 1


col_max, row_max = map(int, input().split())
storage = [list(map(int, input().split())) for _ in range(row_max)]

check_0 = []
tomato = 0
for r in range(row_max):
    for c in range(col_max):
        if storage[r][c] == 0:
            tomato += 1
        elif storage[r][c] == 1:
            check_0.append((r,c))

day = 0
while tomato > 0 and check_0:
    check = []
    for r, c in check_0:
        change(r, c)
    check_0 = check[:]
    day += 1


if tomato > 0:
    print(-1)
else:
    print(day)


# PyPy3: 194212 kb 464ms 
# Python3: 148932 kb 2104ms	
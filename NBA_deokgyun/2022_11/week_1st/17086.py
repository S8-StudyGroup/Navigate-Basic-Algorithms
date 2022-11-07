# BOJ_17086. 아기상어2

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
sharks = []
max_legth = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            sharks.append((i, j))
for i in range(n):
    for j in range(m):
        length_list = []
        for k in range(len(sharks)):
            len_i = abs(sharks[k][0] - i)
            len_j = abs(sharks[k][1] - j)
            length_list.append(len_i if len_i > len_j else len_j)
        safe_length = min(length_list)
        if safe_length > max_legth:
            max_legth = safe_length
print(max_legth)
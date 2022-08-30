# 어디에 단어가 들어갈 수 있을까

T = int(input())

for test_count in range(1, T + 1):
    N, K = map(int, input().split())
    N_list = [list(map(int, input().split())) for _ in range(N)]
    letters_count = 0
    for i in range(N):
        row_sum = 0
        column_sum = 0
        for j in range(N):
            if N_list[i][j] == 0 and row_sum == K:
                letters_count += 1
            if N_list[j][i] == 0 and column_sum == K:
                letters_count += 1
            row_sum = row_sum * N_list[i][j] + N_list[i][j]
            column_sum = column_sum * N_list[j][i] + N_list[j][i]
        if row_sum == K:
            letters_count += 1
        if column_sum == K:
            letters_count += 1

    print(f"#{test_count}", letters_count)

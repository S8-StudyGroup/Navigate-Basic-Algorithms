# 어디에 단어가 들어갈 수 있을까

for test_case in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]

    # 길이가 k인 것만 찾음
    ok = 0
    for i in range(n):
        one1 = 0
        one2 = 0
        for j in range(n):
            if puzzle[i][j] == 1:  # 가로 확인
                one1 += 1
            else:
                if one1 == k:
                    ok += 1
                one1 = 0

            if puzzle[j][i] == 1:  # 세로 확인
                one2 += 1
            else:
                if one2 == k:
                    ok += 1
                one2 = 0
        else:  # 행 또는 열 끝날 때,
            if one1 == k:
                ok += 1
            if one2 == k:
                ok += 1
    print(f'#{test_case} {ok}')


'''
for-else 문 사용하고 싶지 않다면
바깥에 0을 둘러싸줌
'''

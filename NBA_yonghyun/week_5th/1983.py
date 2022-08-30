# 조교의 성적 매기기

grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

for test_case in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    students = [list(map(int, input().split())) for _ in range(n)]

    scores = [0] * n
    for i in range(n):
        scores[i] = 0.35 * students[i][0] + 0.45 * students[i][1] + 0.2 * students[i][2]
        if i == k - 1:
            k_score = scores[i]
    cut = n // 10
    scores = sorted(scores, reverse=True)

    idx = 0
    for i in range(0, n, cut):
        if k_score in scores[i : i + cut]:
            print(f'#{test_case} {grade[idx]}')
            break
        idx += 1

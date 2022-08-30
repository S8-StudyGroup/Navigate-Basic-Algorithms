# 조교의 성적 매기기
score_list = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

T = int(input())

for test_case in range(1, T + 1):

    N, K = map(int, input().split())
    scores = []

    for i in range(1, N + 1):
        m, f, h = map(int, input().split())
        total_score = 0.35 * m + 0.45 * f + 0.2 * h
        scores.append({'idx': i, 'total': total_score})

    scores.sort(key=lambda x: x['total'], reverse=True)
    for i in range(len(scores)):
        if scores[i]['idx'] == K:
            print(f"#{test_case} {score_list[i // (N // 10)]}")
            break

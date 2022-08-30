# 조교의 성적 매기기

# 1983. 조교의 성적 매기기

t = int(input())

standard = ['D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+']

for tc in range(1, t + 1):
    n, k = map(int, input().split())

    scores = []

    # for i in range(n):
    #     a, b, c = map(int, input().split())
    #     scores.append([a * 0.35 + b * 0.45 + c * 20, i + 1])

    for _ in range(n):
        a, b, c = map(int, input().split())
        scores.append(a * 0.35 + b * 0.45 + c * 0.20)

    # scores.sort(key=lambda x: x[0])
    k_score = scores[k - 1]
    score_list = sorted(scores)
    k_order = score_list.index(k_score) + 1

    s = int(n // 10)

    if k_order % s == 0:
        answer = standard[int(k_order // s - 1)]
    else:
        answer = standard[int(k_order // s)]

    print(f'#{tc} {answer}')
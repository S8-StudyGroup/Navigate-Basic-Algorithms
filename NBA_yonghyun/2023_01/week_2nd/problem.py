# [BOJ] 14889. 스타트와 링크


def comb(start, link, depth):
    global min_diff
    global last_start

    if depth == n:
        if len(start) == n // 2:
            if last_start == link:
                print(min_diff)
                exit()

            last_start = start

            start_val = getDiff(start)
            link_val = getDiff(link)
            diff = abs(start_val - link_val)

            if diff < min_diff:
                min_diff = diff

            if min_diff == 0:
                print(min_diff)
                exit()

        return

    comb(start + [player[depth]], link, depth + 1)
    comb(start, link + [player[depth]], depth + 1)


def getDiff(arr):
    fullPower = 0
    for i in range(len(arr) - 1):
        back = arr[i + 1 :]
        for j in back:
            fullPower += power[arr[i]][j] + power[j][arr[i]]
    return fullPower


n = int(input())
power = [list(map(int, input().split())) for _ in range(n)]
player = list(range(0, n))

min_diff = 10000
last_start = []
comb([], [], 0)


'''
메모리도 적게 쓰고 실행속도도 훨씬 빨라짐
다만 걱정은 알고리즘에서 exit를 쓰는 것이 괜찮은가...
(문제는 맞았지만...)
'''

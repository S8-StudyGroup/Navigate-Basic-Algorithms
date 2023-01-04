# [SWEA] 1244. 최대 상금
# 미해결
import sys
sys.setrecursionlimit(100000)


def change(arr):
    if len(arr) == 2:
        card = cards[:]
        card[arr[0]], card[arr[1]] = card[arr[1]], card[arr[0]]
        number = ''
        for i in card:
            number = number + i
        cases.append(int(number))
    start = 0
    if arr:                                 # 두번째 카드 고르는거면
        start = arr[0] + 1                  # 고른 거 다음 인덱스부터 고르도록
    for i in range(start, len(cards)):
        arr.append(i)                       # 추가
        change(arr)
        arr.pop(i)                          # arr리스트에 담은 값 제거


for t in range(1, int(input()) + 1):
    c, n = input().split()
    cards = list(map(str, c))               # 문자열을 리스트로 나누기
    cases = []                              # 모든 경우를 저장

    for _ in range(int(n)):
        change([])

    print(f'#{t} {max(cases)}')

# 1220. Magnetic

for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    for i in range(N):
        prev = 0  # 교착상태 확인 변수
        for j in range(N):  # 세로줄 탐색
            if table[j][i] == 1:  # 붉은 자성체이면
                prev = 1  # prev에 1 저장
            if table[j][i] == 2:  # 푸른 자성체이면
                if prev == 1:  # prev가 1인 경우 교착 상태로 판단하여
                    prev = 0  # prev를 0으로 바꾸고
                    cnt += 1  # 교착상태 개수 + 1
    print(f"#{tc} {cnt}")

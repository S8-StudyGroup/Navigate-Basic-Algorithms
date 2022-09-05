# 어디에 단어가 들어갈 수 있을까

t = int(input())

for tc in range(1, t + 1):
    n, k = map(int, input().split())  # 행렬의 크기 N, 글자수 K
    arr = [list(map(int, input().split())) for _ in range(n)]  # 0,1로 이뤄진 행렬 (0 : 벽, 1 : 단어가 들어갈 수 있는 공간)
    k_cnt = 0  # 단어가 들어갈 수 있는 공간 개수 k_cnt

    # 1) 행 방향으로 연속되는 1 찾기
    for i in range(n):
        cnt = 0  # 행마다 cnt 초기화
        for j in range(n):  # 열 인덱스에 한칸씩 돌면서
            if arr[i][j] == 1:  # 만약 해당 칸이 1이 나온 상태라면(연속한다면)
                cnt += 1  # cnt를 +1 한다

            else:  # 만약 1이 연속되다가 0으로 끊긴다면
                if cnt == k:  # 현재까지 모은 cnt가 k를 달성했는지 확인한다
                    k_cnt += 1  # 만약 달성했다면 단어 개수 k_cnt + 1
                cnt = 0  # k개를 달성하지 못했다면 cnt를 초기화

        ## 오른쪽, 아래 칸을 0으로 둘러쌓이게 이차원 리스트를 조작하면 이 부분이 필요 없음! - 아래 코드 반복되는 게 복잡할수록 효율적일듯!
        if cnt == k:  # 하나의 행을 다 돌았는데 중간에 0이 끊기지 않은 채로 끝났다면
            k_cnt += 1  # k개가 올바르게 연속됐으므로 k_cnt + 1

        
    # 2) 열 방향으로 연속되는 1 찾기
    for j in range(n):
        cnt = 0
        for i in range(n):
            if arr[i][j] == 1:
                cnt += 1

            else:
                if cnt == k:
                    k_cnt += 1
                cnt = 0

        if cnt == k:
            k_cnt += 1

    print(f'#{tc} {k_cnt}')

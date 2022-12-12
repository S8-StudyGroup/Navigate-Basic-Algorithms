# [SWEA] 2112. 보호 필름


# 성능검사
def check(arr):
    for j in range(W):
        prev = arr[0][j]
        cnt = 1  # 동일한 특성의 셀이 연속된 개수

        for i in range(1, D):  # 각 열마다 탐색
            if prev == arr[i][j]:  # 이전 셀과 특성이 동일할 경우
                cnt += 1
                if cnt == K:  # 합격기준에 도달할 경우 더 이상 볼 필요 없음
                    break
            else:
                prev = arr[i][j]  # 특성이 동일하지 않다면
                cnt = 1  # 연속된 개수를 초기화하여 계속 진행
        else:
            return False  # 하나의 열이라도 합격기준 미도달 시 False 반환
    else:
        return True  # 모든 열이 합격기준에 도달했을 경우 True 반환


# 각 행에 대해 약품 투여 여부를 결정하는 dfs
def dfs(idx, cnt):  # idx: 행에 대한 인덱스, cnt: 약품 투여 횟수
    if idx == D:  # 모든 행에 대해 진행했다면
        global min_cnt
        if min_cnt > cnt and check(matrix):  # cnt가 최소 투여 횟수보다 적고 성능검사를 통과했다면
            min_cnt = cnt  # 최소 투여 횟수 교체
        return

    temp = matrix[idx][:]  # 복구를 위한 행 임시 저장

    # 약품 미투여
    dfs(idx + 1, cnt)

    # A약품 투여
    matrix[idx] = [0] * W
    dfs(idx + 1, cnt + 1)
    matrix[idx] = temp[:]  # 원상 복구

    # B약품 투여
    matrix[idx] = [1] * W
    dfs(idx + 1, cnt + 1)
    matrix[idx] = temp[:]  # 원상 복구


T = int(input())

for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(D)]

    if K == 1:  # 합격기준이 1이면 무조건 통과이므로
        print(f"#{tc} 0")  # 0 출력

    else:
        min_cnt = D  # 약품 최소 투여 횟수

        dfs(0, 0)
        print(f"#{tc} {min_cnt}")

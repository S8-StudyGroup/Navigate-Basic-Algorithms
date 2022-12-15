# [Programmers] 77485. 행렬 테두리 회전하기

def solution(rows, columns, queries):

    # 1. 1부터 row*col숫자로 채워진 2차원 배열 만들기
    array = [[0] * columns for _ in range(rows)]

    cnt = 0
    for i in range(rows):
        for j in range(columns):
            cnt += 1
            array[i][j] = cnt

    answer = []
    
    # 2. 회전 정보에 따른 배열 덩어리 이동
    for x1,y1,x2,y2 in queries:
        temp = array[x1-1][y1-1] # 가장 상단 왼쪽 값은 tmp에 따로 보관
        minV = temp              # 해당 값을 초기 최솟값으로 지정

        # ↑ 이동 (y1 고정)
        for k in range(x1-1, x2-1):
            pick = array[k+1][y1-1]
            array[k][y1-1] = pick
            minV = min(minV, pick)

        # ← 로 이동 (x2 고정)
        for k in range(y1-1,y2-1):
            pick = array[x2-1][k+1]
            array[x2-1][k] = pick
            minV = min(minV, pick)

        # ↓ 로 이동 (y2 고정)
        for k in range(x2-1,x1-1,-1):
            pick = array[k-1][y2-1]
            array[k][y2-1] = pick
            minV = min(minV, pick)

        # → 로 이동 (x1 고정)
        for k in range(y2-1,y1-1,-1):
            pick = array[x1-1][k-1]
            array[x1-1][k] = pick
            minV = min(minV, pick)

        array[x1-1][y1] = temp   # 모두 이동한 후 temp에 저장해뒀던 값을 한 칸 오른쪽으로 옮김
        answer.append(minV)     # 현재까지 갱신된 최솟값을 answer에 append

    return answer
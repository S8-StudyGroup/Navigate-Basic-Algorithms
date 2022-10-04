# swea 1949. [모의 SW 역량테스트] 등산로 조성
# import sys
# sys.stdin = open('swea_1949.txt')
'''
1. 가장 높은 봉우리에서 시작
2. 높은 지형에서 낮은 지형으로 가로 또는 세로 방향으로 연결되어야 한다.
3. 딱 한 곳을 정해서 최대 k 깊이만큼 지형을 깎는 공사를 할 수 있다.
가장 긴 등산로의 길이를 출력
'''
d_r = [0, 0, 1, -1]
d_c = [1, -1, 0, 0]


# dfs
def dfs(row, col, length=1, dig=1):
    global k, size, answer

    here_height = board[row][col]           #
    visited[row][col] = True                # 방문처리
    
    if length > answer:                     # 등산로 길이 갱신
        answer = length

    for d in range(4):                      # 상하좌우 방향
        next_r = row + d_r[d]
        next_c = col + d_c[d]

        if 0 <= next_r < size and 0 <= next_c < size and not visited[next_r][next_c]:       # 범위 안, 방문 안한곳이면 진행
            next_height = board[next_r][next_c]
            
            if next_height < here_height:                           # 내리막길이면
                dfs(next_r, next_c, length + 1, dig)                # dfs

            else:                                                   # 내리막길아니면
                if dig == 0:                                        # 공사 횟수 없으면 패스
                    continue
                else:                                               # 공사 횟수 있으면
                    diff = next_height - here_height                # 높이차를 구해서 공사하면 갈수있는지 확인
                    if diff < k:                                    # 
                        board[next_r][next_c] = here_height - 1     # 다음 장소는 현재 높이 - 1 까지만 깎는다
                        dfs(next_r, next_c, length + 1, 0)          # dfs (dig는 0으로 보내준다)
                        board[next_r][next_c] = next_height         # 그쪽 탐색이 끝났으면 공사전으로 되돌리기
                    
                    else:                                           # 공사해도 갈수없으면
                        continue

    visited[row][col] = False               # 방문처리 초기화
                


for case in range(1, int(input()) + 1):
    size, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(size)]

    max_height = max(list(map(max, board)))                         # 높이 최대값 구하고

    visited = [[False] * size for _ in range(size)]                 # 방문 테이블 생성
    answer = 0                                                      # 길이 최대값 담을 변수 생성
    for r in range(size):
        for c in range(size):
            if board[r][c] == max_height:                           # 최대 높이에서 dfs 시작
                dfs(r, c)
    
    print(f'#{case} {answer}')
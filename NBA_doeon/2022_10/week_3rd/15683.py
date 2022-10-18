# [BOJ] 15683. 감시

# 백준 15683. 감시
# time : 30m + (3h + 30m)
# idea
'''
dfs라고 생각했으나 감시 방향이 상하좌우 중 n개로 정해지기만 하면
그 방향대로 list 범위 안, 벽이 아닌 0인 칸인 경우에 쭉 가기만 하면 됨
cctv 종류마다 어떤식으로 표현을 해줘야 사용하기 쉬울지
회전 가능 -> cctv 종류 하나가 여러 상태일 수 있고, 이 상태 중 하나를 선택해야 함

- 델타값 우하좌상 만들고
- 각 시시티비마다 리스트를 줌

- 시작
1. 리스트 돌면서 1~5값이면 해당 cctv 위치를 따로 저장
2. 첫번째 cctv부터 dfs 함수 실행

- dfs
1. 인자 : 현재 보고있는 cctv 순서, 감시 가능한 곳 합 cnt)
2. 가지치기 해줄 것은?
3. 첫번째 cctv를 넣으면서 어떤 모드로 해줄지 같이 넣어줘야 하나? -> 함수 실행 전 for문으로
4. pop되면 가지고 있는 그 위치에서 시작해서 인자로 받아온 모드로 cctv 종류의 몇번째 모드로 할지 정하고
그럼 가져온 그 모드에 적혀진 d의 개수만큼 갈 수 있는 곳만큼 가면서 true로 바꿔주고, cnt + 1 (벽이여도 +1)
-> 아니면 함수 들어와서 for d in range(len(cctv종류))로 해주는 게 나을까?

5.
'''
dx = [0, 1, 0, -1]  # 우하좌상
dy = [1, 0, -1, 0]  # 우하좌상

# cctv의 방향 종류와 그 종류가 볼 수 있는 방향을 기록해둔 딕셔너리
cctv = {1: [[0], [1], [2], [3]],
        2: [(0, 2), (1, 3)],
        3: [(0, 1), (1, 2), (2, 3), (3, 0)],
        4: [(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)],
        5: [(0, 1, 2, 3)]}


def dfs(cnt_cctv, cnt):

    # 1. 종료조건 : 보고자 하는 cctv 개수가 총 개수를 만족하면
    if cnt_cctv == len(pos):
        cnts.append(cnt)    # 현재까지의 감시된 곳 개수 저장
        return              # 종료

    # 2. 종료 전 해야 할 작업
    x, y = pos[cnt_cctv]    # 들어온 cctv 인덱스를 통해 position 리스트에서 좌표값 얻음
    cctv_num = arr[x][y]    # 좌표값에 해당하는 cctv 번호 알아냄

    for mode in range(len(cctv[cctv_num])): # cctv 번호에 따른 종류 개수마다 반복
        can_see = []                        # 종류마다 새롭게 감시 구역이 정해짐

        for d in cctv[cctv_num][mode]:      # 종류마다 () 튜플 안 모든 방향들에 대해서 반복
            nx = x + dx[d]                  # 다음으로 볼 칸
            ny = y + dy[d]

            while 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 6: # 범위 안이고 벽이 아닌 경우 통과 가능
                if arr[nx][ny] == '#' or (1 <= arr[nx][ny] <= 5):   # 만약 이미 감시된 곳 or 다른 cctv가 있는 곳이면
                    nx += dx[d]                                     # 감시된 영역 카운트하지 않고 다음칸으로 이동만 진행
                    ny += dy[d]
                else:                                               # 위 조건 만족하는데 아직 감시 못한 곳이면
                    arr[nx][ny] = '#'                               # #으로 감시 표시해주고
                    cnt += 1                                        # 카운트 + 1
                    can_see.append((nx, ny))                        # 볼 수 있는 곳 저장
                    nx += dx[d]                                     # 다음칸으로 이동
                    ny += dy[d]

        dfs(cnt_cctv + 1, cnt)          # 감시를 하지 않고 넘어가는 경우

        for idx in range(len(can_see)): # can_see에 저장한 이전에 새롭게 #으로 채운 값 되돌리기 작업
            si, sj = can_see[idx]
            arr[si][sj] = 0
            cnt -= 1


n, m = map(int, input().split())
arr = []        # 이차원리스트
pos = []        # cctv 좌표값(x, y)을 저장하는 position 리스트
cnts= []        # 모든 경우마다 총 감시된 칸 수 저장하는 리스트
cnt_wall = 0    # 벽의 개수

for r in range(n):
    row = list(map(int, input().split()))   # 이차원리스트의 한 행을 받아올 때마다
    for c in range(m):
        if 1 <= row[c] <= 5:                # 해당 칸이 cctv면
            pos.append((r, c))              # 그 위치를 저장
        elif row[c] == 6:                   # 만약 벽(6)이면
            cnt_wall += 1                   # 벽의 개수 +1
    arr.append(row)

# print(arr)
# print(pos)

dfs(0, 0)   # dfs(현재 보고자 하는 cctv 인덱스 0, 현재까지 감시된 곳 카운트 0)
# 정답은 m*n에서 len(pos), cnt_wall, 함수 결과로 나온 # cnt를 다 빼주면 그게 사각지대 개수
print(cnts)
print(m * n - len(pos) - cnt_wall - max(cnts))

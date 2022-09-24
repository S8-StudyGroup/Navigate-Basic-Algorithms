# [SWEA] 1220. Magnetic
# Guest - 김도희

for tc in range(1, 11):
    n = int(input()) # 정사각형 테이블의 한 변의 길이
    board = [list(map(int, input().split())) for _ in range(n)] # 테이블의 초기 모습, 1 : n극, 2: s극

    cnt = 0 # 테이블 위에 남아있는 교착 상태의 개수
    for col in range(n): # 열 탐색
        row = 0
        stack = []

        while row < n:
            if not stack and board[row][col] == 1: # stack이 비어있는 상태에서 board에 1이 나오면 stack에 넣는다.
                stack.append(1)
            elif stack and board[row][col] == 2: # stack에 1이 있는 상태에서 board에 2가 나오면 stack에서 pop한 값을 cnt에 더한다.
                cnt += stack.pop()
            row += 1 # 다음 행을 탐색하기 위해 row에 1을 더한다.

    print(f"#{tc} {cnt}")
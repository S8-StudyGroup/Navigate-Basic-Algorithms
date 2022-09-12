# 1220. Magnetic

for tc in range(1, 11):
    n = int(input())    # 행렬의 크기
    cnt = 0             # 교착 개수를 저장할 변수

    arr = [list(map(int, input().split())) for _ in range(n)]
    cols = list(zip(*arr))      # zip함수를 이용하여 자성체들 리스트를 열로 묶음

    for col in cols:            # 열의 묶음마다 특정 열에서의 12가 들어간 개수를 셈
        col_str = ''            # 열을 0을 제외한 숫자만 문자열 형태로 저장하기 위한 변수
        for i in range(n):
            if col[i] != 0:
                col_str += str(col[i])
        # 이제 1,2으로만 이루어진 col의 str 형태가 완성됨
        # col_changed = col_str.replace('12', '.')
        cnt += col_str.count('12')      # 문자열에서 12로 이어진 경우만 카운트해서 횟수 더함

    print(f'#{tc} {cnt}')
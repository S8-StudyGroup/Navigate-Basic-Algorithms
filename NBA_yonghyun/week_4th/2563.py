# 백준 - 색종이

'''
도화지를 위아래로 뒤집은 상태라고 생각하고 풀면 인덱스를 굳이 안 바꿔도 됨
만약 입력이 3 7 이면
[6][2]이 왼쪽 위 꼭짓점인 10x10 정사각형이라고 생각하고 풀면 됨
'''

white = [[0] * 100 for _ in range(100)]  # 흰색 도화지 - 칠하지 않은 부분은 0
t = int(input())  # 색종이의 수

for t in range(t):
    y, x = map(int, input().split())

    for i in range(x - 1, x + 9):  # 행 10번 반복
        for j in range(y - 1, y + 9):  # 열 10번 반복
            white[i][j] = 1  # 색종이의 영역은 1로 바꿈

# 색종이의 영역 계산
cnt = 0
for i in range(100):
    for j in range(100):
        if white[i][j] == 1:
            cnt += 1

print(cnt)

# 백준 - 색종이

# 도화지 크기, 색종이 크기
p_size = 100
n_size = 10

# 색종이 수
n = int(input())
# 색종이 붙인 위치( 왼쪽 변과의 거리, 아래쪽 변과의 거리 )
points = [list(map(int, input().split())) for _ in range(n)]

# 도화지
paper = [[0] * p_size for _ in range(p_size)]

for k in range(n):
    # 왼쪽 변과의 거리인 지점에서 색종이 크기만큼만
    for i in range(points[k][0], points[k][0] + n_size):
        for j in range(points[k][1], points[k][1] + n_size):
            paper[i][j] = 1


area = 0
for i in range(p_size):
    for j in range(p_size):
        if paper[i][j] == 1:
            area += 1

print(area)


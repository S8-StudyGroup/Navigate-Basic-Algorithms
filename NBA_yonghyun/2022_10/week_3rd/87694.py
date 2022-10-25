# [Programmers] 87694. 아이템 줍기


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    return answer


rectangle = [[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]]
solution(rectangle, 1, 3, 7, 8)

dots = []
for rec in rectangle:
    dots.append([rec[0], rec[1]])
    dots.append([rec[0], rec[3]])
    dots.append([rec[2], rec[3]])
    dots.append([rec[2], rec[1]])

print(dots)

start = [1, 3]
itemX = 7
itemY = 8

visited = [False] * len(dots)
move = 0
min_move = 1000000


def find_way(x, y, move):
    global min_move
    if move > min_move:
        return

    for i in range(len(dots)):
        if not visited[i] and x == dots[i][0]:
            if itemX == x and min(y, dots[i][1]) <= itemY <= max(y, dots[i][1]):
                move += max(y, dots[i][1]) - itemY
                if move < min_move:
                    min_move = move
                return
            visited[i] = True
            find_way(x, dots[i][1], move + abs(y - dots[i][1]))
            visited[i] = False

        elif not visited[i] and y == dots[i][1]:
            if itemY == y and min(x, dots[i][0]) <= itemX <= max(x, dots[i][0]):
                move += max(y, dots[i][0]) - itemX
                if move < min_move:
                    min_move = move
                return
            visited[i] = True
            find_way(dots[i][0], y, move + abs(x - dots[i][0]))
            visited[i] = False


border = []

for x1, y1, x2, y2 in rectangle:
    for i in range(x1, x2 + 1):
        border.append([i, y1])
        border.append([i, y2])

    for j in range(y1 + 1, y2):
        border.append([x1, j])
        border.append([x2, j])

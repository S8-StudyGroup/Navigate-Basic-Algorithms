# [Programmers] 87694. 아이템 줍기
# Guest - 박승재


def solution(rectangle, characterX, characterY, itemX, itemY):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    outside_box = set()
    inside_box = set()
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if i == x1 or i == x2 or j == y1 or j == y2:
                    outside_box.add((i, j))
                else:
                    inside_box.add((i, j))
    way = outside_box - inside_box
    characterX, characterY, itemX, itemY = (
        characterX * 2,
        characterY * 2,
        itemX * 2,
        itemY * 2,
    )
    visit = {(characterX, characterY)}
    nx, ny = characterX, characterY
    result = 0
    while True:
        if (nx, ny) == (itemX, itemY):
            answer = result
        for n in range(4):
            new_x, new_y = nx + dx[n], ny + dy[n]
            if (new_x, new_y) in way and (new_x, new_y) not in visit:
                visit.add((new_x, new_y))
                nx, ny = new_x, new_y
                result += 1
                break
        else:
            break

    return min(answer, result - answer + 1) // 2

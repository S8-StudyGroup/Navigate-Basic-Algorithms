# [SWEA] 2112. 보호 필름

from itertools import product


def is_test_passed(film):
    for j in range(col):
        cell = 1
        for i in range(1, row):
            if film[i][j] != film[i - 1][j]:
                cell = 1
            else:
                cell += 1

            if cell >= k:
                break

        if cell < k:
            return False

    return True


def inject_chemicals(film, start, end, film_row):
    global result
    picked_length = len(picked_rows)
    if picked_length == end:
        for chemicals_type in product([0, 1], repeat=picked_length):
            t = 0
            former_row = []
            for picked_row in picked_rows:
                former_row.append((picked_row, film[picked_row][:]))
                for j in range(col):
                    film[picked_row][j] = chemicals_type[t]
                t += 1
            if is_test_passed(film):
                for info in former_row:
                    film[info[0]] = info[1]
                result = end
                return

            for info in former_row:
                film[info[0]] = info[1]

        return

    for i in range(start, film_row):
        picked_rows.append(i)
        inject_chemicals(film, i + 1, end, film_row)
        if result > 0:
            return
        picked_rows.pop()


for test_case in range(1, int(input()) + 1):
    row, col, k = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(row)]
    result = 0

    if not is_test_passed(film):
        for inject in range(1, row + 1):
            picked_rows = []
            inject_chemicals(film, 0, inject, film_row=row)
            if result > 0:
                break

    print(f'#{test_case} {result}')
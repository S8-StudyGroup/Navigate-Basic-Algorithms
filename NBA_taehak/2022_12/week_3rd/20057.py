# [BOJ] 20057. 마법사 상어와 토네이도
import sys
input = sys.stdin.readline

size = int(input())
area = [list(map(int, input().split())) for _ in range(size)]


# area 안에 있는지 확인하는 함수
def inrange(r, c):
    if 0 <= r < size and 0 <= c < size:
        return True
    else:
        return False


# 흩뿌리기
## 좌 하 우 상
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]


def scatter(r, c, di):
    '''
    (r, c): y좌표
    di: 현재 진행 방향
    return: 영역바깥으로 흩뿌려진 모래의 양
    '''
    sand = area[r][c]
    sand10 = int(sand * 0.1)
    sand7 = int(sand * 0.07)
    sand5 = int(sand * 0.05)
    sand2 = int(sand * 0.02)
    sand1 = int(sand * 0.01)

    scattered = 0
    remain = sand - 2 * sand10 - 2 *sand7 - sand5 - 2 *sand2 - 2 *sand1

    a, b = dr[di], dc[di]

    r10_1, c10_1 = r + a + b, c + a + b
    r10_2, c10_2 = r + a - b, c + b - a
    r7_1, c7_1 = r + b, c + a
    r7_2, c7_2 = r - b, c - a
    r5_1, c5_1 = r + 2*a, c + 2*b
    r2_1, c2_1 = r + 2*b, c + 2*a
    r2_2, c2_2 = r - 2*b, c - 2*a
    r1_1, c1_1 = r - a + b, c + a - b
    r1_2, c1_2 = r - a - b, c - a - b
    ra, ca = r + a, c + b

    scatter_list = [
        (r10_1, c10_1, sand10),
        (r10_2, c10_2, sand10),
        (r7_1, c7_1, sand7),
        (r7_2, c7_2, sand7),
        (r5_1, c5_1, sand5),
        (r2_1, c2_1, sand2),
        (r2_2, c2_2, sand2),
        (r1_1, c1_1, sand1),
        (r1_2, c1_2, sand1),
        (ra, ca, remain),
    ]

    area[r][c] = 0
    for sr, sc, ssand in scatter_list:
        if inrange(sr, sc):
            area[sr][sc] += ssand
        else:
            scattered += ssand

    return scattered

r, c = (size // 2, size // 2)
arc = 1
result = 0
di = 0
check = 0
# print('===================================================')
# print((r, c, di))
# for i in area:
#     print(i)

for arc in range(1, size + 1):
    for __ in range(2):
        for _ in range(arc):
            r += dr[di]
            c += dc[di]
            result += scatter(r, c, di)

            check += 1
            # print()
            # print((r, c), di, result)
            # for i in area:
            #     print(i)

        if arc == size:
            break

        di = (di + 1) % 4

    if arc == size:
        break

print(result)

# [BOJ] 20057. 마법사 상어와 토네이도

# 델타 탐색(반시계 방향)
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
cur_x = (N - 1) // 2
cur_y = (N - 1) // 2
sand_out_of_range = 0                                                   # 밖으로 나간 모래의 양
move = 0                                                                # 해당 방향으로 움직일 칸 수

while cur_x != 0 or cur_y != 0:                                         # (0, 0)에 도달하면 종료
    for d in range(4):                                                  # 반시계 방향
        if d % 2 == 0:                                                  # d가 짝수일 때만 칸 수 + 1
            move += 1
        for _ in range(move):                                           # 해당 방향으로의 이동 횟수만큼 반복
            total_side_sand = 0                                         # 주변으로 새는 모래들의 합
            move_x, move_y = cur_x + dx[d], cur_y + dy[d]               # 여기로 토네이도가 올 예정

            for side in [(d + 1) % 4, (d - 1) % 4]:                     # 이동 위치에서의 좌우 방향

                # 7% 칸
                side_x, side_y = move_x + dx[side], move_y + dy[side]
                side_sand = int(matrix[move_x][move_y] * 0.07)
                if 0 <= side_x < N and 0 <= side_y < N:
                    matrix[side_x][side_y] += side_sand
                else:
                    sand_out_of_range += side_sand
                total_side_sand += side_sand

                # 10% 칸
                side_x1, side_y1 = side_x + dx[d], side_y + dy[d]
                side_sand1 = int(matrix[move_x][move_y] * 0.1)
                if 0 <= side_x1 < N and 0 <= side_y1 < N:
                    matrix[side_x1][side_y1] += side_sand1
                else:
                    sand_out_of_range += side_sand1
                total_side_sand += side_sand1

                # 1% 칸
                side_x2, side_y2 = side_x + dx[(d + 2) % 4], side_y + dy[(d + 2) % 4]
                side_sand2 = int(matrix[move_x][move_y] * 0.01)
                if 0 <= side_x2 < N and 0 <= side_y2 < N:
                    matrix[side_x2][side_y2] += side_sand2
                else:
                    sand_out_of_range += side_sand2
                total_side_sand += side_sand2

                # 2% 칸
                side_x3, side_y3 = side_x + dx[side], side_y + dy[side]
                side_sand3 = int(matrix[move_x][move_y] * 0.02)
                if 0 <= side_x3 < N and 0 <= side_y3 < N:
                    matrix[side_x3][side_y3] += side_sand3
                else:
                    sand_out_of_range += side_sand3
                total_side_sand += side_sand3

            # 5% 칸
            front_side_x, front_side_y = move_x + dx[d] * 2, move_y + dy[d] * 2
            front_side_sand = int(matrix[move_x][move_y] * 0.05)
            if 0 <= front_side_x < N and 0 <= front_side_y < N:
                matrix[front_side_x][front_side_y] += front_side_sand
            else:
                sand_out_of_range += front_side_sand
            total_side_sand += front_side_sand

            # 토네이도가 이동할 칸
            final_move_x, final_move_y = move_x + dx[d], move_y + dy[d]
            move_sand = matrix[move_x][move_y] - total_side_sand
            if 0 <= final_move_x < N and 0 <= final_move_y < N:
                matrix[final_move_x][final_move_y] += move_sand
            else:
                sand_out_of_range += move_sand

            matrix[move_x][move_y] = 0      # 토네이도가 이동한 칸을 0으로 초기화

            cur_x, cur_y = move_x, move_y   # 현재 토네이도 위치 갱신

            if cur_x == 0 and cur_y == 0:   # (0, 0) 자리에 왔다면 탈출
                break

        if cur_x == 0 and cur_y == 0:       # (0, 0) 자리에 왔다면 탈출
            break

print(sand_out_of_range)

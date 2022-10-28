# 개미

# 가로 길이가 w 세로 길이가 h 인 2차원 공간, 좌표 (p, q)에 개미
# w, h = map(int, input().split())
# p, q = map(int, input().split())
# hour = int(input())

# # 초기방향
# d_x = 1
# d_y = 1
# p_0 = p
# q_0 = q

# # 한번 움직이기
# def go(p, q, w, h, d_x, d_y):
#     if p == w or p == 0:
#         d_x *= -1
#     if q == h or q == 0:
#         d_y *= -1
#     p += d_x
#     q += d_y
#     return p, q, w, h, d_x, d_y


# # 진행
# count = 0
# for i in range(hour):
#     count += 1
#     p, q, w, h, d_x, d_y = go(p, q, w, h, d_x, d_y)

#     if q == q_0 and p == p_0 and d_x == 1 and d_y == 1:
#         new_hour = hour % count
#         for i in range(new_hour):
#             p, q, w, h, d_x, d_y = go(p, q, w, h, d_x, d_y)
#         break

# print(p, q)


w, h = map(int, input().split())
p, q = map(int, input().split())
hour = int(input())

# x, y 좌표 따로 따로 계산하기

x_count = hour % (2 * w)
y_count = hour % (2 * h)

#
x_dir = 1
for _ in range(x_count):
    if p == w or p == 0:
        x_dir *= -1
    p += x_dir

y_dir = 1
for _ in range(y_count):
    if q == h or q == 0:
        y_dir *= -1
    q += y_dir

print(p, q)

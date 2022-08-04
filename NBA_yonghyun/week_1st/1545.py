# 거꾸로 출력해 보아요


num = int(input())

num_list = list(range(num + 1))


for i in sorted(num_list, reverse=True):
    print(i, end=' ')

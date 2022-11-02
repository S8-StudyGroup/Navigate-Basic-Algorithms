# BOJ_10158. 개미

col, row = map(int, input().split())
now_j, now_i = map(int, input().split())
hour = int(input())

if ((hour + now_i) // row) % 2:
    result_i = row - ((hour + now_i) % row)
else:
    result_i = (hour + now_i) % row

if ((hour + now_j) // col) % 2:
    result_j = col - ((hour + now_j) % col)
else:
    result_j = (hour + now_j) % col

print(result_j, result_i)
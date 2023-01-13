# [BOJ] 2755. 이번학기 평점은 몇점?
# https://www.acmicpc.net/problem/2755

score_dict = {
    'A+' : 4.3,
    'A0': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B0': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C0': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D0': 1.0,
    'D-': 0.7,
    'F': 0.0
}

allpoint = [0,0]
for i in range(int(input())):
    eachline = input().split()
    point = int(eachline[1])
    allpoint[0] += score_dict[eachline[2]] * point
    allpoint[1] += point
result = allpoint[0] / allpoint[1]
print("%.2f" %(round(allpoint[0] / allpoint[1] + 10 ** -10)))
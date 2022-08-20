# 대각선 출력하기

for i in range(5):
    for j in range(5):
        print("#" if i == j else "+", end="")
    print()

# 대각선 출력하기

for i in range(5):
    for j in range(i):
        print('+', end='')
    print('#', end='')
    for j in range(4-i):
        print('+', end='')
    print()
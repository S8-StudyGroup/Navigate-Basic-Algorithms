# 대각선 출력하기
print('#++++')
print('+#+++')
print('++#++')
print('+++#+')
print('++++#')

for i in range(5):
    print('+' * i, end='')
    print('#', end='')
    print('+' * (4-i))

for i in range(5):
    print('+' * i, '#', '+' * (4-i), sep='')
# 거꾸로 출력해 보아요

# range의 숫자를 역순으로 생성하려면 증가 폭을 음수로 지정
# ex. range(10, 0, -1)는 10부터 1까지 -1씩 증가하는 숫자를 생성

num = int(input())

for number in range(num, -1, -1): ## num에서 0까지 -1씩 줄어드는 range
    print(number, end=' ')

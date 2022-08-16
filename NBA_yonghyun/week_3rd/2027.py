# 대각선 출력하기

'''
[ 아이디어 ]


insert + for문으로 위치 지정

언패킹으로 출력

다시 삭제

부호 사이에 띄어쓰기 없어야 함 =>  sep=''

'''

plus = ['+'] * 4

for i in range(5):
    plus.insert(i, '#')
    print(*plus, sep='')
    plus.pop(i)

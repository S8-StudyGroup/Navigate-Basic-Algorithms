# 날짜 계산기
##아이디어:  월만 표시된 365개의 원소를 가진 리스트(달력)을 만들어 놓고  첫번째 날짜의 인덱스를 찾고,  두번째 날짜의 인덱스를 찾아서,  둘 사이의 차이를 계산한다.


tc = int(input())  ##테스트 케이스 개수

for i in range(tc):
    date = list(map(int, input().split()))  ## date는  ex) 3 10 5 14 ,  3월 10일부터  5월 14일까지 얼마나 떨어져 있는가?

    calender = [1] * 31 + [2] * 28 + [3] * 31 + [4] * 30 + [5] * 31 + [6] * 30 + [7] * 31 + [8] * 31 + [9] * 30 + [
        10] * 31 + [11] * 30 + [
                   12] * 31  ## 365개의  원소를 가지는 리스트  ex) [1, 1, 1, 1 ..., 2, 2, 2, .... 3, 3, 3, ... ...12, 12, 12, 12]

    for k in range(len(calender)):  ## 첫번째 날짜의 인덱스를 찾기.  찾고자 하는 month를 발견하면 그것의 index에다가 일 수만큼 더해주고 1은 빼준다.
        if calender[k] == date[0]:
            index_1 = k + date[1] - 1
            break

    for k in range(len(calender)):
        if calender[k] == date[2]:
            index_2 = k + date[3] - 1
            break

    result = index_2 - index_1 + 1  ##최종 결과

    print(f'#{i + 1} {result}')


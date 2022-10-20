# 4013. 특이한 자석
##문제풀이 아이디어: 톱니바퀴 번호와 방향이 주어지면, 같이 돌아가게될 톱니바퀴를 조사한다. 그 결과를 temp라는 리스트에 넣는다.
## [1, -1, 0, 0]인 경우 1번 톱니는 시계방향, 2번톱니는 반시계방향, 3,4번 톱니는 움직이지 않는다.
## 조사가 끝나면, temp에 적혀있는대로 톱니바퀴를 움직인다. 그리고 이 과정을 주어진 횟수 rot_number만큼 반복한뒤, 점수를 계산한다.


def rot(rot_num, rot_inf, origin_wheel):                                   ##움직이는 횟수, 회전에 관련된 정보, 최초의 톱니바퀴 정보를 인자로 받는다.
    for m in range(rot_num):                                               ##움직이는 횟수만큼 과정을 반복할것임.
        k = rot_inf[m][0]                                                  ##회전에 관련된 정보는 이차원 리스트 형태로 받음 ex)[[1, 1], [3, -1]].  k는 m+1번째 회전의 바퀴번호
        h = rot_inf[m][1]                                                  ## h는 m+1번째 회전의 회전방향.
        temp = [0, 0, 0, 0]
        temp[k - 1] = h                                                    ## k번째 바퀴의 회전방향 표시 해놓기.

        while k + 1 <= 4 and origin_wheel[k - 1][2] != origin_wheel[k][6]:        ## 오른쪽부터 같이 회전할 바퀴가 있는지 조사할것. 4번째를 넘어가지 않고, 접촉부분의 극성이 다른지 확인.
            k = k + 1                                                             ## 조건을 만족하면 다음 바퀴번호로 k를 바꾸기.
            h = h * (-1)                                                          ## 방향은 반대로
            temp[k - 1] = h                                                       ## temp에 바퀴 정보 넣어놓기.

        k = rot_inf[m][0]                                                      ## 왼쪽을 조사하기 위해 시작했던 바퀴번호와 회전방향 다시 넣기.
        h = rot_inf[m][1]

        while k - 1 >= 1 and origin_wheel[k - 1][6] != origin_wheel[k - 2][2]:  ## 마찬가지로 왼쪽 조사
            k = k - 1
            h = h * (-1)
            temp[k - 1] = h

        for j in range(4):                                                     ## 조사가 끝난뒤 temp를 돌면서 알맞게 바퀴 회전하기.
            if temp[j] == 1:
                origin_wheel[j].insert(0, origin_wheel[j].pop())

            if temp[j] == -1:
                origin_wheel[j].append(origin_wheel[j].pop(0))
    result = 0
    for f in range(4):                                                         ## 마지막으로 점수 계산하기.
        result += origin_wheel[f][0] * (2**f)
    return result


tc = int(input())
for i in range(tc):
    rot_number = int(input())
    wheel = [list(map(int, input().split())) for _ in range(4)]
    rot_informaiton = [list(map(int, input().split())) for _ in range(rot_number)]
    print(f'#{i + 1} {rot(rot_number, rot_informaiton, wheel)}')
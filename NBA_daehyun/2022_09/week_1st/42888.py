# 42888. 오픈채팅방
def solution(record):
    id_set = set()  ##유저들의 id를 담을 집합
    for i in record:  ##레코드를 순회하면서 id부분만을 집합에 담기.
        a = i.split()
        id_set.add(a[1])

    id_nick_dict = {
        i: 0 for i in id_set
    }  ##각각의 id를 key로 지정하고, value는 0으로 되어있는 딕셔너리 만들어놓기.

    for i in record:
        a = i.split()  ##레코드를 순회하면서 Leave가 아니라면 방금 만든 딕셔너리에 각 id에 해당하는 닉네임 value로 변경.
        if a[0] != 'Leave':  ##계속 변경하다보면 각 id마다 최신 닉네임을 value로 가지게 될것.
            id_nick_dict[i.split()[1]] = i.split()[2]

    result = []  ##결과를 담을 빈 리스트.
    for i in record:  ##레코드를 순회하면서 각 id마다 행동에 맞게 닉네임 + 들어오기/나가기 문구 써서 result에 append.
        a = i.split()
        if a[0] == 'Enter':
            result.append(id_nick_dict[a[1]] + '님이 들어왔습니다.')
        elif a[0] == 'Leave':
            result.append(id_nick_dict[a[1]] + '님이 나갔습니다.')

    answer = result

    return answer


#     id_nick_list = dict()                                    ##원래 이렇게 2중 포문으로 하였는데 32개 테스트 케이스중 마지막 7개가 시간초과났습니다.
#     for i in id_set:                                         ##다른 사람 코드를 보고 힌트를 얻었습니다.  안그랬으면 못풀었을거에요 ㅜㅜ
#         for j in record[::-1]:
#             if j[1] == i and (j[0] != 'Leave'):
#                 id_nick_list[i] = j[2]
#                 break
#             else:
#                 continue

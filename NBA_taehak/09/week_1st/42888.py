# 42888. 오픈채팅방

# list.index => O(n), dict['key'] => O(1)


def solution(record):

    user_list = dict()

    for i in record:
        i = i.split()
        if i[0] == 'Enter' or i[0] == 'Change':
            user_list[i[1]] = i[2]

    answer = []

    for i in record:
        i = i.split()
        if i[0] == 'Enter':
            answer.append(f'{user_list[i[1]]}님이 들어왔습니다.')
        elif i[0] == 'Leave':
            answer.append(f'{user_list[i[1]]}님이 나갔습니다.')

    return answer

# 42888. 오픈채팅방


def solution(record):
    answer = []  # 최종출력
    codes = []  # 유저 id 값
    names = dict()  # id 당 유저 이름
    status = []  # 나갔는지 들어왔는지
    for index, text in enumerate(record):
        text_ls = text.split()
        word = text_ls[0]
        code = text_ls[1]
        if len(text_ls) == 3:
            user = text_ls[2]

        if word == 'Enter':
            codes.append(code)
            status.append('님이 들어왔습니다.')
            names[code] = user
        elif word == 'Leave':
            codes.append(code)
            status.append('님이 나갔습니다.')
        elif word == 'Change':
            names[code] = user

    for i, code in enumerate(codes):
        answer.append(names[code]+status[i])

    return answer



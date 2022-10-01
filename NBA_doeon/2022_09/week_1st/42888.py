# 42888. 오픈채팅방

def solution(record):
    answer = []
    mode_list = {'Enter': '들어왔습니다.', 'Leave': '나갔습니다.'}
    id_nickname = dict()

    # 1. 유저아이디-닉네임 연결한 딕셔너리 만들기
    for i in range(len(record)):
        if 'Enter' in record[i] or 'Change' in record[i]:
            mode, userid, nickname = record[i].split()
            id_nickname[userid] = nickname

    # 2. Enter, Leave일 때만 값 받아서 answer에 출력 형식대로 저장
    for i in range(len(record)):
        if 'Leave' in record[i]:
            mode, userid = record[i].split()
            answer.append(f'{id_nickname[userid]}님이 {mode_list[mode]}')

        elif 'Enter' in record[i]:
            mode, userid, nickname = record[i].split()
            answer.append(f'{id_nickname[userid]}님이 {mode_list[mode]}')
    
    return answer
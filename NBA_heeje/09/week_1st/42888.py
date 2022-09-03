# 42888. 오픈채팅방


def solution(record):
    answer = []  # 메세지 출력하는 리스트
    user_info = {}  # 유저의 아이디와 닉네임을 저장
    for rec in record:
        message = rec.split()
        if message[0] == "Enter":
            user_info[message[1]] = message[2]
            answer.append([message[1], "님이 들어왔습니다."])
        elif message[0] == "Leave":
            answer.append([message[1], "님이 나갔습니다."])
        else:
            user_info[message[1]] = message[2]
    # 예시
    # user_info -> {"uid1234": "Prodo", "uid4567": "Ryan"}
    # answer -> [
    # ["uid1234", "님이 들어왔습니다."],
    # ["uid4567", "님이 들어왔습니다."],
    # ["uid1234", "님이 나갔습니다."],
    # ["uid1234", "님이 들어왔습니다."],
    # ]

    # 원하는 형식으로 변환
    answer = [user_info[msg[0]] + msg[1] for msg in answer]
    return answer

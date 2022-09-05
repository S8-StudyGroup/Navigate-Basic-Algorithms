# 42888. 오픈채팅방

def solution(record):
    user_id = []
    user_nickname = []
    result = []
    for info in record:
        info = info.split()
        if len(info) == 3:
            user_id.append(info[1])
            user_nickname.append(info[2])
    user_info = {user_id[_]: user_nickname[_] for _ in range(len(user_id))}

    for sentence in record:
        sentence = sentence.split()
        if sentence[0] == "Enter":
            result.append(f'{user_info[sentence[1]]}님이 들어왔습니다.')

        elif sentence[0] == "Leave":
            result.append(f'{user_info[sentence[1]]}님이 나갔습니다.')

    # 시간 초과 일어난 코드
    # 시간초과 일어난 이유 분석 : 딕셔너리의 값을 찾아갈 때 key값을 바로 대입하면 되는데 반복문으로 찾아서
    # for sentence in record:
    #     sentence = sentence.split()
    #     if sentence[0] == "Enter":
    #         for key, value in user_info.items():
    #             if key == sentence[1]:
    #                 result.append(f'{value}님이 들어왔습니다.')
    #                 break
    #     elif sentence[0] == "Leave":
    #         for key, value in user_info.items():
    #             if key == sentence[1]:
    #                 result.append(f'{value}님이 나갔습니다.')
    #                 break
    #
    
    answer = result
    return answer

# 예시 출력 확인용
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))

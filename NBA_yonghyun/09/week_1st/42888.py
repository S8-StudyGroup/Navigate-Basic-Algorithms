# 42888. 오픈채팅방

# Enter, Leave => 메시지를 출력해야 함
# Enter, Change => 닉네임을 저장 또는 수정해야 함


def solution(record):
    result = []  # 출력할 결과
    user = {}  # 사용자의 아이디와 닉네임을 담을 딕셔너리
    command_list = []  # 명령과 사용자의 아이디를 담을 리스트

    for i in range(len(record)):
        # 1. Enter 명령이 들어왔을 때,
        if record[i][:5] == "Enter":
            # 명령, 아이디, 닉네임을 나눠줌
            command, user_id, name = record[i].split()
            # user 딕셔너리에 아이디:닉네임 쌍을 넣어줌
            user.update({user_id: name})
            # command_list에 실행할 명령과 그 아이디를 넣어줌
            command_list.append([command, user_id])

        # 2. Leave 명령이 들어왔을 때,
        elif record[i][:5] == "Leave":
            # 명령, 아이디를 나눠줌 (닉네임은 받지 않음)
            command, user_id = record[i].split()
            # command_list에 실행할 명령과 그 아이디를 넣어줌
            command_list.append([command, user_id])

        # 3. Change 명령이 들어왔을 때,
        elif record[i][:6] == "Change":
            # 명령, 아이디, 닉네임을 나눠줌
            command, user_id, name = record[i].split()
            # user 딕셔너리 안에 있는 해당 user_id의 닉네임을 바꿔줌
            user.update({user_id: name})

    # 메시지 저장
    # 닉네임이 바뀌면 이전 메시지의 닉네임까지 전부 바뀌어야 해서 조건문을 따로 빼주었다
    for i in range(len(command_list)):
        # Enter 명령일 때, 해당 아이디의 닉네임을 넣은 문장 저장
        if command_list[i][0] == "Enter":
            result.append(f'{user.get(command_list[i][1])}님이 들어왔습니다.')
        # Leave 명령일 때, 해당 아이디의 닉네임을 넣은 문장 저장
        elif command_list[i][0] == "Leave":
            result.append(f'{user.get(command_list[i][1])}님이 나갔습니다.')

    # print(result)

    return result


solution(
    [
        "Enter uid1234 Muzi",
        "Enter uid4567 Prodo",
        "Leave uid1234",
        "Enter uid1234 Prodo",
        "Change uid4567 Ryan",
    ]
)

# 42888. 오픈채팅방


def solution(record):
    answer = []
    people = {}
    for i in record:
        # 들어온 리스트의 요소를 받아서 공백을 기준으로 split
        person_action = i.split()  # person_action = ["Enter", "uid1234", "Muzi"]
        if len(person_action) == 3:  # Enter 혹은 Change라서 길이가 3이라면
            people.update({person_action[1]: person_action[2]})  # {유저 아이디 : 닉네임}으로 딕셔너리 추가
        if person_action[0] == "Enter":  # Enter라면 "유저아이디 + 님이 들어왔습니다.""
            answer.append(f"{person_action[1]}님이 들어왔습니다.")
        elif person_action[0] == "Leave":  # Leave라면 "유저아이디 + 님이 나갔습니다."
            answer.append(f"{person_action[1]}님이 나갔습니다.")
    for j in range(len(answer)):  # answer 리스트를 순회하면서
        user_id = answer[j].split("님")[0]  # '님'을 기준으로 나눠서 앞부분 즉 유저 아이디를 저장
        answer[j] = answer[j].replace(user_id, people[user_id])  # 이후 리스트의 문자열 속 유저아이디를 현재 닉네임으로 수정

    return answer

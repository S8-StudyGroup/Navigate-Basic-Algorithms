# [Programmers] 72410. 신규 아이디 추천

def solution(new_id):
    # 1단계 : 소문자 치환 - lower 함수 이용
    new_id_level1 = new_id.lower()

    # 2단계 : 완전 탐색으로 유효성 검사 진행
    # isalpha() : 알파벳이면 true, isdigit() : 숫자이면 true
    new_id_level2 = ""
    for c in new_id_level1:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            new_id_level2 += c

    # 3단계 : 연속된 마침표를 하나의 마침표로 치환
    new_id_level3 = ""
    is_dot = False  # 이전 문자가 마침표인지 알려주는 변수
    for c in new_id_level2:  # 완전 탐색
        if c != ".":  # 현재 문자가 마침표가 아닌 경우
            if is_dot:  # 이전 문자가 마침표였다면
                is_dot = False  # 변수를 false로 변환 후
            new_id_level3 += c  # 현재 문자를 new_id_level3에 넣어준다.

        else:  # 현재 문자가 마침표일 경우
            if not is_dot:  # 이전 문자가 마침표가 아닐 경우에만
                is_dot = True  # 변수를 true로 변환 후
                new_id_level3 += "."  # 현재 문자(마침표)를 new_id_level3에 넣어준다.

    # 4단계 : 처음 또는 끝에 위치한 마침표 제거 - strip 함수 이용
    new_id_level4 = new_id_level3.strip(".")

    # 5단계 : 빈 문자열이라면 "a" 삽입
    new_id_level5 = new_id_level4 if new_id_level4 else "a"

    # 6단계 : 길이가 16자 이상이라면 15자까지만 저장
    # 제거 후 마침표가 끝에 위치한다면 마침표 제거
    new_id_level6 = new_id_level5 if len(new_id_level5) < 16 else new_id_level5[:15].rstrip(".")

    # 7단계 : 2자 이하라면 3자가 될 때까지 마지막 문자를 반복
    new_id_level7 = new_id_level6
    while len(new_id_level7) <= 2:
        new_id_level7 += new_id_level6[-1]

    # 최종 아이디 반환
    return new_id_level7
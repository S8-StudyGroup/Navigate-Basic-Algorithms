# [Programmers] 72410. 신규 아이디 추천

def solution(new_id):
    answer = ''

    # 1단계 : 모든 대문자를 소문자로 치환
    new_id = new_id.lower()
    # 2단계 : 알파벳 소문자, 숫자, -, _, .,를 제외한 모든 문자 소거
    for letter in new_id:
        if letter.islower() or letter.isdigit() or letter in ['-', '_', '.']:
            answer = answer + letter
    # 3단계 : 마침표(.)가 2번이상 연속된 부분을 하나로 만들기
    dot_cnt = answer.count('.')
    for i in range(dot_cnt, 1, -1):
        dot = '.' * i
        answer = answer.replace(dot, '.')
    # 4단계 : 마침표가 처음이나 끝에 위치한다면 제거
    while answer and answer[0] == '.':
        answer = answer[1:]
    while answer and answer[-1] == '.':
        answer = answer[:-1]
    # 5단계 : 빈문자열이라면 a를 대입
    if len(answer) == 0:
        answer = 'aaa'
    # 6단계 : 16자 이상이면 첫 15개 이후로 제거, 그 후 마침표가 처음이나 마지막에 있다면 제거
    if len(answer) >= 16:
        answer = answer[:15]
    while answer and answer[0] == '.':
        answer = answer[1:]
    while answer and answer[-1] == '.':
        answer = answer[:-1]
    # 7단계 : 2자 이하라면 마지막 문자를 길이가 3이 될때까지 반복
    while len(answer) <= 2:
        answer = answer + answer[-1]

    return answer

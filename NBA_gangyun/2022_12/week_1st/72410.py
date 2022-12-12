# [Programmers] 72410. 신규 아이디 추천

def solution(new_id):
    # 1단계
    new_id = new_id.lower()

    # 2단계
    allowed_string = {'-', '_', '.'}
    replaced_id = ''
    for char in new_id:
        if char.isalpha() or char.isdecimal() or char in allowed_string:
            replaced_id += char
    new_id = replaced_id

    # 3단계
    replaced_id = ''
    dot_count = 0
    for char in new_id:
        if char == '.':
            dot_count += 1
        else:
            dot_count = 0
        if dot_count < 2:
            replaced_id += char
    new_id = replaced_id

    # 4단계
    if new_id[:1] == '.':
        new_id = new_id.lstrip('.')
    if new_id[-1:] == '.':
        new_id = new_id.rstrip('.')

    # 5단계
    if new_id == '':
        new_id += 'a'

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id.rstrip('.')

    # 7단계
    if len(new_id) <= 2:
        last_char = new_id[-1]
        while len(new_id) != 3:
            new_id += last_char

    answer = new_id
    return answer
# [Programmers] 72410. 신규 아이디 추천

def solution(new_id):
    # 1, 2, 3
    condition = {'-', '_'}
    memo = '.'
    for char in new_id:
        if char.isalpha():
            memo += char.lower()
        elif char.isdecimal():
            memo += char
        elif char in condition:
            memo += char
        elif char == '.' and memo[-1] != '.':
            memo += char
    
    # 4
    memo = memo.strip('.')

    # 5
    if memo == '':
        memo = 'a'

    # 6
    if len(memo) >= 16:
        memo = memo[:15]
    memo = memo.rstrip('.')

    # 7
    while len(memo) < 3:
        memo += memo[-1]        

    return memo


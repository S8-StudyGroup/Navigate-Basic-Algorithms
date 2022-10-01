# [Programmers] 17681. [1차] 비밀지도

def solution(n, arr1, arr2):
    rests_1 = []    # arr1의 이진수 변환 결과 (리스트 형태)
    rests_2 = []    # arr2의 이진숫 변환 결과
    map = [['#'] * n for _ in range(n)]  # 초기 지도 (모두 '#'으로 채워진 이차원리스트)
    answer = []     # 최종 지도의 각 행을 문자열 형태로 저장할 출력 리스트

    # 1. arr1 숫자들을 이진수로 변환함
    for i in range(len(arr1)):
        rest = [0] * n  # 한 숫자마다의 나머지 저장 리스트 - [0, 0, 0, ... 0] 형태
        num = arr1[i]   # arr의 한 숫자를 num으로 받음
        j = n - 1       # 나머지 저장 리스트의 끝에서부터 나머지 값을 할당

        while num != 0: # 몫이 0이 될 때까지
            rest[j] = num % 2   # 2로 나눈 나머지를 저장 리스트에 할당
            num = num // 2      # 몫을 업데이트
            j -= 1              # rest 리스트 한 칸 앞으로 옮김

        # rest 출력
        # [0, 1, 0, 0, 1]
        # [1, 0, 1, 0, 0]
        # [1, 1, 1, 0, 0]
        # [1, 0, 0, 1, 0]
        # [0, 1, 0, 1, 1]

        rests_1.append(rest)    # 위 rest들을 이차원리스트로 저장

    # 2. arr2의 숫자들을 이진수로 변환함
    for i in range(len(arr2)):
        rest = [0] * n
        num = arr2[i]
        j = n - 1

        while num != 0:
            rest[j] = num % 2
            num = num // 2
            j -= 1

        rests_2.append(rest)

    # 3. 두 나머지 2차원 리스트를 돌면서 둘 다 0인 경우만 map 원소를 공백으로 변환함
    for r in range(n):
        for c in range(n):
            if rests_1[r][c] == 0 and rests_2[r][c] == 0:
                map[r][c] = ' '

    # 4. map의 각 행마다 문자열로 변환 후 리턴값에 저장
    for row in range(n):
        one_row = ''.join(map[row])
        answer.append(one_row)

    return answer
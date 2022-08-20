# 간단한 압축풀기

'''
[ 아이디어 ]

map 함수로 입력받기

문자 개수만큼 넣은 리스트 생성

for 문 사용하여 출력
슬라이싱

'''

t = int(input())

for test_case in range(1, t + 1):

    print(f'#{test_case}')

    all = []  # 모든 문자를 넣을 리스트

    n = int(input())

    for _ in range(n):

        alp, num = input().split()

        for _ in range(int(num)):
            all.append(alp)

    # 한줄에 10개씩 출력하기 위해 all 리스트의 길이를 10으로 나눈 몫만큼 반목문 실행
    # 나눈 몫 * 10에서부터 10개까지 슬라이싱 통해 출력
    for i in range(len(all) // 10 + 1):
        print(*all[i * 10 : i * 10 + 10], sep='')

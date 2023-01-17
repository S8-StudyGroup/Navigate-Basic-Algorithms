# [BOJ] 18870. 좌표 압축

n = int(input())
numbers = list(map(int, input().split()))

numbers_exist = sorted(set(numbers))
numbers_dict = dict()

# 숫자가 키, 압축개수가 밸류인 딕셔너리 만들기
for i in range(len(numbers_exist)):
    numbers_dict[numbers_exist[i]] = i

answer = []

for case in numbers:
    answer.append(numbers_dict[case])
    
    ## 1. 딕셔너리에 존재 숫자들을 1 값으로 넣어두고 작은 수인 키의 밸류를 더해가는 방법 -> 시간초과
    # sum = 0
    # for nb in numbers_exist:
    #     if nb >= case:
    #         break
    #     else:
    #         sum += numbers_dict[nb]
    # answer.append(sum)

    ## 2. index() 함수 사용 -> 시간초과
    # answer = []
    # for nb in numbers:
    #     answer.append(numbers_exist.index(nb))
    #
    # print(*answer)

print(*answer)

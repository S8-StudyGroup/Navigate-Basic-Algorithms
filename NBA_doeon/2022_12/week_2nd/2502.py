# [BOJ] 2502. 떡 먹는 호랑이

day, cnt = map(int, input().split())

memo = [0 for _ in range(day)]  # memo : 떡 개수를 저장할 리스트
print(memo)
# memo = [1번째 날 떡 개수, 2번째 개수, ..., day번째 개수]
memo[0] = 1 # A 초기값 : 정해져있지 않으므로 1로 시작 (1 <= A <= B)
memo[1] = 1 # B 초기값 : "

ing = True  # 현재 답을 찾았는지에 대한 확인 변수

while ing:  # [1, 1] 로 시작해서 모든 경우를 완전탐색
    # 1. 현재 memo 리스트 값대로 memo 끝까지 피보나치로 memo 완성
    for i in range(2, day):
        memo[i] = memo[i - 1] + memo[i - 2]

    # 2-1. 만약 현재 완성한 memo 리스트의 day번째 날 개수가 cnt와 같다면 -> 해당 memo가 정답
    if memo[day - 1] == cnt:
        print(memo[0])
        print(memo[1])
        break

    # 2-2. 현재 day번째 날 개수가 결과여야 할 개수보다 크다면? -> 차이를 좁혀야 하므로 1번째 개수 +1
    elif memo[day - 1] > cnt:
        memo[0] += 1
        memo[1] = memo[0]

    # 2-3. 현재 memo대로 day번째 날 개수가 cnt보다 작다면? -> 차이를 키워야 하므로 2번째 날 개수 + 1
    elif memo[day - 1] < cnt:
        memo[1] += 1
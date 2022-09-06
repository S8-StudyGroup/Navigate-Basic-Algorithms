# 2635. 수 이어가기

first = int(input())  # 입력으로 받는 첫 번째 수
cnt = 0  # 개수
arr = []  # 배열

for second in range(1, first + 1):  # 두 번째 수는 첫 번째 수와 같거나 작음
    number = [first, second]  # 첫 번째 수와 두 번째 수는 규칙을 따르지 않으므로, 미리 배열에 넣어준다.
    n = 0  # 수의 순서

    # 음의 정수가 만들어질 때까지 반복
    while True:
        # 양의 정수 또는 0 이라면 배열에 해당 수를 넣고, 다음 순서의 수를 만드는 과정으로 돌아간다.
        if number[n] - number[n + 1] >= 0:
            number.append(number[n] - number[n + 1])
            n += 1
        # 음의 정수라면 이 수를 버리고 더 이상 수를 만들지 않는다.
        else:
            break

    # 최대 개수와 비교
    if cnt < len(number):
        cnt = len(number)
        arr = number

print(cnt)
print(*arr)

# 1대1 가위바위보

# 방법1 : 노가다

# A, B 입력 받아 저장
a, b = map(int, input().split())

# A가 이기는 경우, A를 출력
if (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
    print('A')

# 아니면 B를 출력
else:
    print('B')

# 방법2 : 배열

# a, b = map(int, input().split())
# rps = [0, 1, 2, 3, 1]

# print('B') if b == rps[a + 1] else print('A')

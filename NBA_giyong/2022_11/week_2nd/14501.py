# [BOJ] 14501. 퇴사
n = int(input())
arr = [list(map(int, (input().split()))) for _ in range(n)]

answer = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    if i + arr[i][0] > n:
        answer[i] = answer[i + 1]

    else:
        result = answer[i + arr[i][0]] + arr[i][1]
        if result > answer[i + 1]:
            answer[i] = result
        else:
            answer[i] = answer[i + 1]

print(max(answer))

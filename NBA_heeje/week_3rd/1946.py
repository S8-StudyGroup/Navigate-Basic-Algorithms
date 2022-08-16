# 간단한 압축풀기
T = int(input())
for test_case in range(1, T + 1):
    A = int(input())
    ans = ""
    for i in range(A):
        alp, count = map(str, input().split())
        for j in range(int(count)):
            ans += alp
    print(f"#{test_case}")
    while len(ans) > 0:
        print(ans[0:10])
        ans = ans[10:]

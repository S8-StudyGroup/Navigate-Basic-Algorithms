# 간단한 압축풀기

T = int(input())

for test_case in range(1, T + 1):

    A = int(input())
    ans = ""

    for i in range(A):
        # 알파벳과 개수는 자료형이 다르므로 주의!
        alp, count = input().split()

        # count가 현재 문자열이므로 int로 변환
        ans += alp * int(count)

    # 10개씩 끊어서 출력
    print(f"#{test_case}")
    while len(ans) > 0:
        print(ans[0:10])
        ans = ans[10:]

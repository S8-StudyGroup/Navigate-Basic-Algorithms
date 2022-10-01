# 간단한 압축풀기

for test_case in range(1, int(input()) + 1):
    N = int(input())
    word_zip = ''
    print_word = ''
    for _ in range(N):
        word_info = list(input().split())
        word_zip += word_info[0] * int(word_info[1])

    print(f'#{test_case}')
    for i in range(0, len(word_zip)):
        if i % 10 == 0:
            print(word_zip[i : i + 10 :])

# 간단한 압축풀기

for t in range(1, int(input()) + 1):
    n = int(input())
    contents = []
    c = []
    k = []
    for i in range(n):
        f = input()
        contents = f.split()
        c.append(contents[0])
        k.append(int(contents[1]))

    count = 0  # 10개 출력시 다음 줄로 변경
    print(f'#{t}')
    for i, v in enumerate(k):
        for j in range(v):
            if count == 10:
                print()
                count = 0
            print(c[i], end='')
            count += 1
    print()
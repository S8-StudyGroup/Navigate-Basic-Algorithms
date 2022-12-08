# [BOJ] 2502. 떡 먹는 호랑이


def chk():
    for i in range(1, 100000):
        for j in range(i, 100000):
            temp_list = [i, j]
            for _ in range(D - 2):
                temp_list.append(temp_list[-2] + temp_list[-1])
            if temp_list[-1] == K:
                return [i, j]
            elif temp_list[-1] > K:
                break


D, K = map(int, input().split())

answer = chk()
print(*answer, sep="\n")

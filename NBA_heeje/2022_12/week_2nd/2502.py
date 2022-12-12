# [BOJ] 2502. 떡 먹는 호랑이

# 완전 탐색
def chk():
    for i in range(1, 100000):  # 첫째 날에 준 떡의 개수 찾기
        for j in range(i, 100000):  # 둘째 날에 준 떡의 개수 찾기
            temp_list = [i, j]  # 메모이제이션

            # 해당 경우에서 D번째 날에 준 떡의 개수 구하기
            for _ in range(D - 2):
                temp_list.append(temp_list[-2] + temp_list[-1])

            if temp_list[-1] == K:  # 구한 떡의 개수가 K와 같으면 반환
                return [i, j]
            elif temp_list[-1] > K:  # 구한 떡의 개수가 K보다 크면 반복문 종료
                break
                # 구한 떡의 개수가 K보다 작으면 반복문 계속 진행


D, K = map(int, input().split())

answer = chk()
print(*answer, sep="\n")  # 첫째 날과 둘째 날 출력

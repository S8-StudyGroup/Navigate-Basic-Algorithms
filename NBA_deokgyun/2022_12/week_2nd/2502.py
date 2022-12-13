# [BOJ] 2502. 떡 먹는 호랑이

# 우선 피보나치 수열
# 그 후 정수해를 구하기

# 1. A
# 2. B
# 3. A + B    1 1
# 4. A + 2B   1 2
# 5. 2A + 3B  2 3
# 6. 3A + 5B  3 5
# 7. 5A + 8B  5 8
# A : 1 1 2 3 5 피보나치 수열의 n-2번째 수
# B : 1 2 3 5 8 피보나치 수열의 n-1번째 수


nums = [0]
day, ddeok = map(int, input().split())
for i in range(1, day):
    if i == 1 or i == 2:
        nums.append(1)
        continue
    nums.append(nums[-2] + nums[-1])
Anum, Bnum = nums[day - 2 : day]
# Anum * A + Bnum * B = ddeok
for B in range(1, ddeok // Bnum + 1):
    A = (ddeok - Bnum * B) // Anum
    if (ddeok - Bnum * B) % Anum or A > B:
        continue
    print(A, B, sep="\n")
    break

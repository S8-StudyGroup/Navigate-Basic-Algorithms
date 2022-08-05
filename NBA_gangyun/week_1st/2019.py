# 더블더블

# ---첫번째 제출---
# num = int(input())
# num_double = 1

# for i in range(num + 1):
#     if i == 0:
#         num_double = 1    # 2의 0제곱 == 1
#     else :
#         num_double *= 2   # i가 반복한 횟수만큼 2가 곱해짐
#     print(num_double, end=' ')

a = int(input())
b = 0.5

for i in range(a + 1):
    b *= 2  # if문을 없애기 위해 b를 '0.5*2 = 1'에서 시작
    print(int(b), end=' ')  # 명시적 형변환 이용, float형 출력을 방지

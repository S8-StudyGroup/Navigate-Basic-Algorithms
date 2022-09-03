# 서랍의 비밀번호
## 000 ~ 999 까지의 범위 내에서 주어진 값들 차 비교

pw, first_num = map(int, input().split())

if pw >= first_num: # pw가 주어진 수보다 큰 경우 -> 차이 연산
    result = pw = first_num + 1

else: # pw가 주어진 수보다 작은 경우 
    # -> 999까지 세고 넘어가기 때문에 주어진 수에서 999에서 간 다음, pw까지 가는 횟수 고려
    result = 999 - first_num + pw + 1 

print(result)
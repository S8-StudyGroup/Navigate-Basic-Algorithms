# 날짜 계산기

t = int(input())
# days : 1월부터 12월까지의 일수를 담은 리스트
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for tc in range(1, t + 1):
    # start_m, start_d, end_m, end_d : 시작 월, 시작 일, 끝 월, 끝 일
    start_m, start_d, end_m, end_d = map(int, input().split())
    # result : 총 날짜 수
    result = 0
    
    # 시작 월과 끝 월이 같은 경우 -> 시작 일, 끝 일만 비교하면 됨
    if start_m == end_m:
        result = end_d - start_d + 1
    
    # 시작 월과 끝 월이 다른 경우 -> 월과 월 사이에 존재하는 다른 월들의 값 더함
    else:
        # 시작 월, 끝 월만 고려한 일수
        result += days[start_m - 1] - start_d + end_d + 1
        
        # 월이 start_m과 end_m 사이값이라면 해당 월의 총 일수를 result에 반영
        for i in range(12):
            if start_m < i + 1 < end_m:
                result += days[i]
                
    print(f'#{tc} {result}')
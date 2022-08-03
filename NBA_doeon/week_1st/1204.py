# 최빈수 구하기

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    t = int(input())
    grades = list(map(int, input().split()))
    max_count = 0
    max_i = 0
    
    for i in range(len(grades)):
        counts = grades.count(grades[i])
        if counts > max_count:
            max_count = counts
            max_i = i
            
    print(f'#{t} {grades[max_i]}')
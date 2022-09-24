# [Programmers] 17681. [1차] 비밀지도

def trans_2(n, remain):                ##remain에 []들어감, 2진수로 바꿔주는 함수
    if n // 2 == 0:
        remain.append(n % 2)
        return remain[::-1]
    else:
        remain.append(n % 2)
        return trans_2(n // 2, remain)


def solution(n, arr1, arr2):
    answerr = []
    for i in range(n):
        map_1 = arr1[i]
        map_2 = arr2[i]
        
        map_1_2 = trans_2(map_1, [])   ##2진수로 변환된 값 담기.
        map_2_2 = trans_2(map_2, [])
        
        if len(map_1_2) < n:           ## n자리 수로 만들어주기.
            r = n - len(map_1_2)
            for _ in range(r):
                map_1_2.insert(0, 0)
        if len(map_2_2) < n:
            r = n - len(map_2_2)
            for _ in range(r):
                map_2_2.insert(0, 0)
        
        tmp = []      
        for j in range(n):
            tmp.append(map_1_2[j] or map_2_2[j]) ## or 연산
        
        result = ''
        for p in range(n):
            if tmp[p] == 1:
                result += '#' 
            else:
                result += ' '
        
        
        answerr.append(result)
            
    answer = answerr
    return answer
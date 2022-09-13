# 60058. 괄호 변환

def solution(p):
    answer = ''
    result = 0
    
    
    def find_pair(str):
        nonlocal answer
        
        # 1. 입력 빈 문자열이면 빈 문자열을 반환
        if not str:
            answer += ''
            return
            # return answer
            
        
        # 2-1. 첫 번째 분리 : u 생성하기 (u는 균형잡힌 괄호 문자열)
        u = ''
        stack = []
        cnt_left = 0 # 왼쪽 괄호 개수
        cnt_right = 0 # 오른쪽 괄호 개수
    
        for token in str:   # token을 하나씩 u에 붙이면서 균형잡힌 괄호 문자열까지 끊음
            if (cnt_left == 0 and cnt_left == 0) or (cnt_left != cnt_right): 
                if token == '(':
                    u += token
                    cnt_left += 1
                
                elif token == ')':
                    u += token
                    cnt_right += 1
            else:   # 왼쪽, 오른쪽 괄호 개수가 0이 아니고 둘의 개수가 같아지면 거기까지를 u로 함
                break
    
        # print('cnt_l', cnt_left)
        # print('u', u)
    

        # 여기까지 첫 번째 u가 완성됨!
        # 2-2. v 생성하기 -> u를 제외한 부분이니까 슬라이싱으로 생성
        v = str[(cnt_left + cnt_right):]
    
        # print('v', v)
    
    
        # 3. u가 올바른지 판단하기 위해서 stack을 이용
        for token in u:
            if token == '(':
                stack.append(token)
            elif stack and token == ")":
                stack.pop(-1)
            
        # print('stack', stack)
    
        # 올바른 경우와 아닌 경우 검사 -> stack이 비어있는지 확인 (비어있음 -> 올바름)
        if not stack:               # 3-1. 올바른 괄호 문자열 만족하면 v에 대해 1단계부터!
            answer += u             # u는 올바르니까 answer에 붙이고
            find_pair(v)            # v에 대해서 또 검사시키기
            return answer
        
        else:                       # 4. 현재 u도 올바른 문자열 아니면 
            answer += '('           # 1) '(' 붙임
            # answer += find_pair(v)
            find_pair(v)            # 2) v에 대하여 1단계부터 실행하여 반환값 붙임
            answer += ')'           # 3) ')' 붙임
        
            u_part = u[1:len(u) - 1]    # 4) u의 처음과 끝을 제외한 u_part 생성
            u_new = ''
            
            for u_part_token in u_part: # u_part의 요소를 반대로 바꿔서 새로운 문자열 생성
                if u_part_token == '(':
                    u_new += ')'
                else:
                    u_new += '('
                    
            answer += u_new             # 새로운 문자열을 answer에 붙임
            return answer
            
        # return answer       
        # print(answer)
            
        
    # return answer
    # print('print', find_pair(p))
    result = find_pair(p)
    # print('result', result)
    return result
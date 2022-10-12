# [Programmers] 64061. 크레인 인형뽑기 게임

def solution(board, moves):
    size = len(board)
    depth = {x:0 for x in range(size)}

    answer = 0
    stack = [0]
    for move in moves:
        move -= 1

        if depth[move] >= size:
            continue

        try:
            while board[depth[move]][move] == 0:
                depth[move] += 1
        except:
            continue
        
        
        if stack[-1] == board[depth[move]][move]:
            stack.pop()
            answer += 2
        else:
            stack.append(board[depth[move]][move])

        depth[move] += 1

    return answer 
        


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))
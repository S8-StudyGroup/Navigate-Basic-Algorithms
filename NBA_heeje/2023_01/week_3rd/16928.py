# [BOJ] 16928. 뱀과 사다리 게임

def bfs():
    queue = [1]
    visited = [False] * 101
    visited[1] = True
    turn = 0
    while queue:
        turn += 1
        for _ in range(len(queue)):
            n = queue.pop(0)
            for i in range(1, 7):
                move = n + i
                if 0 < move <= 100 and not visited[move]: 
                    if move == 100:
                        return turn
                    
                    visited[move] = True
                    if move in ladder_or_snake.keys():
                        queue.append(ladder_or_snake[move])
                    else:
                        queue.append(move)
                    

N, M = map(int, input().split())
ladder_or_snake = dict()
for _ in range(N + M):
    x, y = map(int, input().split())
    ladder_or_snake[x] = y

print(bfs())
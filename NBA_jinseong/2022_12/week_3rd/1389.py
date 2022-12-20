# [BOJ] 1389. 케빈 베이컨의 6단계 법칙

def bfs(num):
    visited = [0] * (N + 1)
    queue = [num]
    visited[num] = 1

    while queue:
        now = queue.pop(0)
        for next in rel[now]:
            if visited[next] == 0:
                visited[next] = visited[now] + 1
                queue.append(next)
    return sum(visited) - N


N, M = map(int, input().split())

rel = [[] for _ in range(N + 1)]                # 친구 관계 저장
kb_num = [0] * (N + 1)                          # 해당 유저의 케빈베이컨 수 저장

for i in range(M):
    a, b = map(int, input().split())
    rel[a].append(b)
    rel[b].append(a)

for i in range(1, N + 1):
    kb_num[i] = bfs(i)

kb_min = min(kb_num[1:])
answer = 0

for i in range(1, N + 1):
    if kb_num[i] == kb_min:
        answer = i
        break

print(answer)


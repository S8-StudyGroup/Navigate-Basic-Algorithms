# [BOJ] 1389. 케빈 베이컨의 6단계 법칙


def bfs(n):
    visited = [0] * (N + 1)
    visited[n] = 1                                  # 자기자신을 1로 뒀으니 나중에 1 * N만큼 빼줘야 함
    queue = [n]

    while queue:
        v = queue.pop(0)
        for w in adj_list[v]:
            if visited[w] == 0:
                visited[w] = visited[v] + 1
                queue.append(w)
    return sum(visited) - N                         # (visited의 합) - (유저 수 N)이 케빈 베이컨 수


N, M = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]               # 인접 리스트

for _ in range(M):
    f1, f2 = map(int, input().split())              # 양방향 그래프
    adj_list[f1].append(f2)
    adj_list[f2].append(f1)

min_sum_kevin_bacon = 99999999                      # 최소 케빈 베이컨 수의 합
idx = -1                                            # 케빈 베이컨 수의 합이 가장 적은 사람의 인덱스
for i in range(1, N + 1):
    sum_kevin_bacon = bfs(i)                        # 각 유저마다 bfs 실행
    if min_sum_kevin_bacon > sum_kevin_bacon:       # 저장된 최소 케빈 베이컨 수와 현 유저의 케빈 베이컨 수 비교 및 갱신
        min_sum_kevin_bacon = sum_kevin_bacon
        idx = i

print(idx)

# [BOJ] 14501. 퇴사

def dfs(nowlocation=0, totalsum=0):
    global maxtotalsum, n
    if nowlocation > n:
        return
    elif nowlocation == n:
        if totalsum > maxtotalsum:
            maxtotalsum = totalsum
        return
    dfs(nowlocation + dayslist[nowlocation][0], totalsum + dayslist[nowlocation][1])
    dfs(nowlocation + 1, totalsum)
    


n = int(input())
dayslist = [tuple(map(int, input().split())) for _ in range(n)]
maxtotalsum = 0
dfs()
print(maxtotalsum)
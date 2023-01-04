# 등수 매기기

numarr = []
numcnt = int(input())
for i in range(numcnt):
    numarr.append(int(input()))
numarr.sort()
leastnum = 0
for i in range(1, numcnt + 1):
    leastnum += abs(numarr[i - 1] - i)
print(leastnum)

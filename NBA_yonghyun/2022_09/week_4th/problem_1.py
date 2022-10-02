# 파일 이름을 문제 번호로 수정해주신 뒤 발표할 문제에 대한 풀이를 작성해주세요!
# 여러 개의 문제를 가져오셨다면 파일을 복사해서 추가로 작성해주시기 바랍니다!


# 백준 1991. 트리 순회
# https://www.acmicpc.net/problem/1991

# 전위탐색
def preorder(i):
    print(alp[i], end='')
    if ch[i] != 0:
        if ch[i][0] != 0:
            preorder(alp.index(ch[i][0]))
        if len(ch[i]) >= 2:
            preorder(alp.index(ch[i][1]))


# 중위탐색
def inorder(i):
    if ch[i] != 0:
        if ch[i][0] != 0:
            inorder(alp.index(ch[i][0]))
        print(alp[i], end='')
        if len(ch[i]) >= 2:
            inorder(alp.index(ch[i][1]))
    else:
        print(alp[i], end='')


# 후위탐색
def postorder(i):
    if ch[i] != 0:
        if ch[i][0] != 0:
            postorder(alp.index(ch[i][0]))
        if len(ch[i]) >= 2:
            postorder(alp.index(ch[i][1]))
    print(alp[i], end='')


n = int(input())
alp = [0] * n
ch = [0] * n
for i in range(n):
    a, left, right = input().split()
    alp[i] = a
    if left != '.':
        ch[i] = [left]
        if right != '.':
            ch[i].append(right)
    elif right != '.':
        ch[i] = [0, right]

preorder(0)
print()
inorder(0)
print()
postorder(0)

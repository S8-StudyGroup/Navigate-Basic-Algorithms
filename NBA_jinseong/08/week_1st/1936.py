# 1대1 가위바위보
ls = input().split()
a = int(ls[0])
b = int(ls[1])
# 1->2, 2->3, 3->1 : +1이면 이기므로 B가 이기는 경우
if ((a % 3) + 1) == b:
    print('B')
elif ((b % 3) + 1) == a:
    print('A')
else:
    pass

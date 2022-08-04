# 1대1 가위바위보

a, b = map(int, input().split())


if a > 1:
    if a == b + 1:
        print("A")
    else:
        print("B")
else:
    if b == 3:
        print("A")
    else:
        print("B")

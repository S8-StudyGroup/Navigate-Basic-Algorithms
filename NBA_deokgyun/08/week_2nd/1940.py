# 가랏! RC카!

import sys


def RCaccel(gear):
    if gear == "0":
        return 0
    elif gear[0] == "1":
        return int(gear[2])
    else:
        return -int(gear[2])


sys.stdin = open("input.txt")

T = int(input())

for i in range(1, T + 1):
    N = int(input())
    RCspeed = 0
    RCdistance = 0
    for _ in range(N):
        RCspeed += RCaccel(input())
        if RCspeed < 0:
            RCspeed = 0
        RCdistance += RCspeed

    print(f"#{i} {RCdistance}")

# 서랍의 비밀번호

p, k = map(int, input().split())

print(p - k + 1)


# -------------------

# p 가 k 보다 무조건 크다는 조건이 문제에 명시되어 있지 않음

if p >= k:
    print(p - k + 1)
else:
    print(999 - k + p + 2)

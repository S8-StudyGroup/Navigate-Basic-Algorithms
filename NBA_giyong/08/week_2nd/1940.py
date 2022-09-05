# 가랏! RC카!
t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    m = 0  # 이동한 거리
    m_s = 0
    for i in range(n):
        s = list(map(int, input().split()))
        if s[0] == 1:
            m_s += s[1]
            m += m_s
        elif s[0] == 2:
            m_s -= s[1]
            if m_s < 0:
                m_s = 0
            m += m_s
        else:
            m += m_s
    print(f"#{tc} {m}")
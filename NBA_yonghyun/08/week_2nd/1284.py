# 수도 요금 경쟁


T = int(input())

for test_case in range(1, T + 1):
    p, q, r, s, w = map(int, input().split())

    # 수도요금이 B사 기준 기본요금만 청구될 때
    if w <= r:
        if p * w > q:
            print(f'#{test_case} {q}')
        else:
            print(f'#{test_case} {p * w}')

    else:
        if p * w > q + (w - r) * s:
            print(f'#{test_case} {q + (w - r) * s}')
        else:
            print(f'#{test_case} {p * w}')

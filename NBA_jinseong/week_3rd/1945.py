
# 간단한 소인수분해

for t in range(1, int(input()) + 1):
    n = int(input())
    small_num = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}

    for num in small_num.keys():
        cnt = 0
        while True:
            # 소인수로 나눠지면 나눈 몫을 저장하고 카운트
            if n % num == 0:
                n //= num
                cnt += 1
            else:
                break
        small_num[num] = cnt

    print(f'#{t}', *small_num.values())
# [SWEA] 2477. 차량 정비소

T = int(input())
for tc in range(1, T + 1):
    N, M, K, A, B = map(int, input().split())
    a_list = list(map(int, input().split()))    # 접수 창고 소요 시간 리스트
    b_list = list(map(int, input().split()))    # 정비 창고 소요 시간 리스트
    t_list = list(map(int, input().split()))    # 고객 방문 시간 리스트
    time = -1                                   # 시간
    completed_customers = 0                     # 정비까지 끝낸 손님의 수
    answer = []                                 # 지갑을 두고 간 고객과 같은 접수, 정비 창고를 이용한 고객 리스트

    customer = 1                                # 손님 index
    customer_info = {}                          # 손님 정보(접수, 정비 창고 번호)

    waiting_receipt = []                        # 접수 대기 리스트
    doing_receipt = [[0, 0] for _ in range(N)]  # 접수 창고 이용 리스트(손님 index, 현재 소요 시간)
    waiting_repair = []                         # 정비 대기 리스트
    doing_repair = [[0, 0] for _ in range(M)]   # 수리 창고 이용 리스트(손님 index, 현재 소요 시간)

    while completed_customers < K:              # 모든 손님이 완료할 때까지 반복

        time += 1

        # 순서 중요!
        # 1. 도착하는 손님 확인
        # 2. 접수 완료된 손님을 정비 대기 리스트로 이동
        # 3. 접수 대기중인 손님을 접수 창고 이용 리스트로 이동
        # 4. 정비 완료된 손님을 보내면서 문제에서 요구하는 정답과 일치하는지 비교
        # 5. 정비 대기중인 손님을 정비 창고 이용 리스트로 이동

        # 도착하는 손님 확인
        while t_list and t_list[0] == time:
            waiting_receipt.append(customer)
            customer_info[customer] = [0, 0]
            customer += 1
            t_list.pop(0)

        # 접수 완료
        for i in range(N):
            if doing_receipt[i][0] != 0:
                doing_receipt[i][1] += 1
                if doing_receipt[i][1] == a_list[i]:
                    waiting_repair.append(doing_receipt[i][0])
                    doing_receipt[i] = [0, 0]
        # 대기자 접수
        if waiting_receipt:
            for i in range(N):
                if doing_receipt[i][0] == 0:
                    doing_receipt[i][0] = waiting_receipt.pop(0)
                    customer_info[doing_receipt[i][0]][0] = i + 1
                    if not waiting_receipt:
                        break

        # 정비 완료
        for i in range(M):
            if doing_repair[i][0] != 0:
                doing_repair[i][1] += 1
                if doing_repair[i][1] == b_list[i]:
                    if customer_info[doing_repair[i][0]] == [A, B]:
                        answer.append(doing_repair[i][0])
                    doing_repair[i] = [0, 0]
                    completed_customers += 1
        # 대기자 정비
        if waiting_repair:
            for i in range(M):
                if doing_repair[i][0] == 0:
                    doing_repair[i][0] = waiting_repair.pop(0)
                    customer_info[doing_repair[i][0]][1] = i + 1
                    if not waiting_repair:
                        break

    print(f"#{tc} {sum(answer) if answer else -1}")

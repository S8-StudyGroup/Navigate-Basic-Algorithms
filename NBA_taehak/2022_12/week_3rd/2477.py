# [SWEA] 2477. 차량 정비소
for case in range(1, int(input()) + 1):
    n, m, k, c_n, c_m = map(int, input().split())
    n_times = list(map(int, input().split()))
    m_times = list(map(int, input().split()))
    c_times = list(map(int, input().split()))
    
    # {창구번호: [(고객번호, 다시 사용 가능 시간;접수창구에서 정비창구로 가는시간), ...], ...}
    pass_n_list = {x:[(0, 0)] for x in range(1, n + 1)}
    pass_m_list = {x:[(0, 0)] for x in range(1, m + 1)}
    
    # 고객이 온 순서대로 탐색 (@@1)
    for idx, time in enumerate(c_times, start=1):
        can_go_n = []
        wait_n = [0, 99999]

        # 창구 조사
        for n_idx, n_info in pass_n_list.items():
            # 가장 빨리 비게 되는 창구 갱신
            if n_info[-1][-1] < wait_n[-1]:
                wait_n = [n_idx, n_info[-1][-1]]
            
            # 현재 시간보다 빠르게 비어있는 창구를 만나면 그만 탐색(고객이 오면 바로 들어올 창구)
            if time >= n_info[-1][-1]:
                can_go_n.append(n_idx)
                break
        
        if can_go_n:
            pass_n_list[can_go_n[0]].append((idx, time + n_times[can_go_n[0]-1]))
        else:
            pass_n_list[wait_n[0]].append((idx, wait_n[1] + n_times[wait_n[0]-1]))
    
    # 접수창구에서 나오는 고객정보
    from_n = list()
    for n_num, n_list in pass_n_list.items():
        for i in n_list:
            from_n.append((*i, n_num))
    
    # 시간순, 접수창구번호순
    from_n.sort(key=lambda x: x[-1])
    from_n.sort(key=lambda x: x[-2])
    
    # @@1 과 동일
    for idx, time, n_num in from_n:
        if idx == 0:
            continue
        can_go_m = []
        wait_m = [0, 999999]
        for m_idx, m_info in pass_m_list.items():
            if m_info[-1][-1] < wait_m[-1]:
                wait_m = [m_idx, m_info[-1][-1]]
            if time >= m_info[-1][-1]:
                can_go_m.append(m_idx)
                break
        if can_go_m:
            pass_m_list[can_go_m[0]].append((idx, time + m_times[can_go_m[0]-1]))
        else:
            pass_m_list[wait_m[0]].append((idx, wait_m[1] + m_times[wait_m[0]-1]))
 
    n_set = set()
    m_set = set()
    for c_num, time in pass_n_list[c_n]:
        n_set.add(c_num)
    for c_num, time in pass_m_list[c_m]:
        m_set.add(c_num)
     
    result = n_set & m_set
 
    if sum(result) == 0:
        print(f'#{case} {-1}')
    else:
        print(f'#{case} {sum(result)}')
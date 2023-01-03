# BOJ_13335. 트럭
from collections import deque

n, bridge_length, bridge_max_weight = map(int, input().split())
truck_weight = deque(map(int, input().split()))

bridge = deque(0 for _ in range(bridge_length))
arrived = deque()
count = 0

while len(arrived) != n:
    if bridge[0] == 0:
        if truck_weight and sum(bridge) + truck_weight[0] <= bridge_max_weight:
            bridge.rotate(-1)
            bridge[-1] = truck_weight.popleft()
        else:
            bridge.rotate(-1)
    else:
        arrived_truck = bridge.popleft()
        arrived.append(arrived_truck)
        if truck_weight and sum(bridge) + truck_weight[0] <= bridge_max_weight:
            bridge.append(truck_weight.popleft())
        else:
            bridge.append(0)
    count += 1
print(count)

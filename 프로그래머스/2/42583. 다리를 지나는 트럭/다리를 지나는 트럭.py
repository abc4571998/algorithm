from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 경과 시간
    count = 0
    queue = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    
    current_weight = 0
    while queue:
        # 현재 트럭의 무게 올라갈 수 있는 트럭 무게를 넘었는지 확인
        count += 1
        current_weight -= bridge.popleft()
        next_truck = queue.popleft()
        
        if current_weight + next_truck > weight:
            bridge.append(0)
            queue.appendleft(next_truck)
        else:
            bridge.append(next_truck)
            current_weight += next_truck
        
    count += bridge_length
    return count
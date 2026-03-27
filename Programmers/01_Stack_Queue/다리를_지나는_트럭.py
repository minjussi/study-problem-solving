# 문제 해결 포인트: 0으로 채워서 시간의 흐름 표현하기
# collections에서 deque를 활용해 큐 문제를 해결할 수 있다

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)  # 리스트를 넣어주기 [0, 0, 0] 이런 식으로
    truck_weights = deque(truck_weights) # 리스트 자체를 삽입 (반복문 사용 가능)
    current_weight = 0 
    
    while bridge:
        time += 1
        passed_truck = bridge.popleft()
        current_weight -= passed_truck
        
        if truck_weights:
            if current_weight + truck_weights[0] <= weight:
                next_truck = truck_weights.popleft()
                bridge.append(next_truck)
                current_weight += next_truck
            else:
                bridge.append(0)

    return time

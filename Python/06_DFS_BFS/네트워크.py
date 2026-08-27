# 넓이 탐색의 원리
# 1. vistied = [False] * n : n개의 컴퓨터가 있으니 그곳을 방문했는지 안 했는지 확인
# 2. 방문을 하지 않았으면, 그 컴퓨터와 연결된 모든 곳들을 탐색 (이걸 하려면 deque를 무조건 써야하는 것!)
# 2-1. [1, 1, 0]이라 되어 있으니까 [False, False, False] 되어 있는 것에서 [True, True, False]가 되는 것
# 3. 그 다음 visited[1]을 확인하면 True니까 건너뛰기
# 4. visited[2]는 False니까 +1 하고 다시 탐색 [0, 0, 1]

from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        # False인 것부터 시작
        if not visited[i]:
            answer += 1
            # queue에 인덱스 자체가 삽입(i=0이면 queue에는 0이 들어감)
            # not visited이면, 그 인덱스를 대기열에 넣어서 첫 번째와 이어진 것을 찾을 수 있게 됨
            queue = deque([i])
            visited[i] = True
            # 연결된 것이 있다면 (대기열이 존재하면)
            while queue:
                # 현재 큐에 들어 있는 번호를 뺀다
                current = queue.popleft()
                # 여기에서 [1, 1, 0] 이렇게 된 그래프를 확인하는 것임!
                for neighbor in range(n):
                    if current != neighbor and computers[current][neighbor] == 1 and not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
    return answer

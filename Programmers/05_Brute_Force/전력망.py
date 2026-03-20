# 기본 문제 풀이 아이디어: 

def solution(n, wires):
    answer = float('inf')
    graph = [[] for _ in range(n + 1)]
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    def dfs(node, visited):
        visited[node] = True 
        count = 1            
        
        for next_node in graph[node]:
            if not visited[next_node]:
                count += dfs(next_node, visited)   
        return count
    
    for v1, v2 in wires:
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        visited = [False] * (n + 1)  
        count1 = dfs(v1, visited)   
        count2 = n - count1
        diff = abs(count1 - count2)
        if diff < answer:
            answer = diff
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    return answer


# BFS 사용 풀이

from collections import deque

def bfs(start, graph, n):
    queue = deque([start])
    visited = [False] * (n + 1) # 송전탑 번호가 1번부터 시작하니까 n+1개 만들기
    visited[start] = True
    count = 1 # 시작점 자기 자신도 1개로 치고 시작!
    
    while queue:
        current = queue.popleft()
        for next_node in graph[current]:
            # 길(전선)이 이어져 있고, 아직 안 가본 송전탑이면?
            if not visited[next_node]: 
                visited[next_node] = True
                queue.append(next_node) # 대기열에 넣고
                count += 1                     
    return count

def solution(n, wires):
    answer = float('inf') # 최솟값을 찾을 거니까 일단 엄청 큰 수로 설정
    
    # 🗺️ 1단계: 컴퓨터가 알아볼 수 있게 전체 지도(그래프) 만들기
    graph = [[] for _ in range(n + 1)]
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    # ✂️ 2단계: 전선 하나씩 가위로 잘라보기
    for v1, v2 in wires:
        # 양쪽 송전탑의 연결 리스트에서 서로를 지워버리기 (싹둑!)
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        
        # 🐕 3단계: 한쪽(v1)에만 탐지견을 풀어서 개수 세어오기
        count1 = bfs(v1, graph, n)
        
        # ⚖️ 4단계: 수학의 마법으로 차이 계산
        count2 = n - count1 # 반대쪽 덩어리 개수
        diff = abs(count1 - count2) # 두 덩어리의 차이 (절댓값)
        
        if diff < answer:
            answer = diff # 기존보다 차이가 더 작으면 정답 갱신!
            
        # 🩹 5단계: 다음 전선을 잘라보기 위해, 방금 잘랐던 전선은 다시 붙여놓기!
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    return answer

# 기본 문제 풀이 아이디어: 첫 번째 전선부터 잘라보면서 두 전력망의 송전탑 개수를 세어
# 절댓값을 비교해 최솟값을 찾는다
# 3가지 풀이법 존재 - 모두 다 좋은 알고리즘이므로 복습 필수 !!
# DFS/BFS - 컴퓨터가 인식하기 쉽게 그래프(인접 리스트) 먼저 제작.
# union find(서로소 집합) - 전선으로 송전탑이 이어지면, 
#                          두 송전탑의 제일 위에 있는 송전탑을 찾아서 합병 

# DFS 사용 풀이 
def solution(n, wires):
    answer = float('inf')
    
    # 인접한 것들을 나타내는 그래프 먼저 제작 !!
    graph = [[] for _ in range(n + 1)]
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    def dfs(node, visited):
        visited[node] = True 
        count = 1  # 자기 자신    
        
        for next_node in graph[node]:
            if not visited[next_node]:
                count += dfs(next_node, visited)   
        return count
        
    for v1, v2 in wires:
        # 전선 자르기
        graph[v1].remove(v2)
        graph[v2].remove(v1)

        visited = [False] * (n + 1)  # 초기화
        count1 = dfs(v1, visited)    # 개수 세기(한 쪽만 세어도 됨)
        
        count2 = n - count1
        diff = abs(count1 - count2) # 절댓값 계산
        if diff < answer:
            answer = diff
            
        # 전선 다시 이어 붙이기
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    return answer


# BFS 사용 풀이
from collections import deque

def bfs(start, graph, n):
    queue = deque([start])
    visited = [False] * (n + 1) # 송전탑 번호가 1번부터 시작하니까 n+1개 만들기
    visited[start] = True
    count = 1 # 시작점 자기 자신도 1개로 치고 시작
    
    while queue:
        current = queue.popleft()
        for next_node in graph[current]:
            # 전선이 이어져 있고, 아직 안 가 본 송전탑
            if not visited[next_node]: 
                visited[next_node] = True
                queue.append(next_node) # 대기열에 넣고
                count += 1          
    return count

def solution(n, wires):
    answer = float('inf')

    graph = [[] for _ in range(n + 1)]
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    for v1, v2 in wires:
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        count1 = bfs(v1, graph, n)
        count2 = n - count1 
        diff = abs(count1 - count2)
        if diff < answer:
            answer = diff 
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    return answer


# 프로그래머스에서 발견한 풀이(서로소집합(disjoint set) 혹은 union find)

uf = []

def find(a):
    global uf
    if uf[a] < 0: return a
    uf[a] = find(uf[a])
    return uf[a]
    
# 합병
def merge(a, b):
    global uf
    pa = find(a)
    pb = find(b)
    if pa == pb: return
    uf[pa] += uf[pb]
    uf[pb] = pa

def solution(n, wires):
    global uf
    answer = int(1e9)
    k = len(wires)
    for i in range(k):
        uf = [-1 for _ in range(n+1)] # 모든 송전탑을 -1로 초기화 (가장 상위에 있는 송전탑으로 설정)
        tmp = [wires[x] for x in range(k) if x != i]
        for a, b in tmp: 
            merge(a, b) # 합병해 나가면 -> 두 전력망 각각의 송전탑 개수 바로 구할 수 있음
        v = [x for x in uf[1:] if x < 0]
        answer = min(answer, abs(v[0]-v[1]))

    return answer

# dfs와 bfs를 모두 사용하는 알고리즘
# 모든 경우의 수를 탐색 -> dfs
# k번 열어서 최대로 감염시키는 개수 세기 -> bfs(물론 dfs 해도 됨 but, 헷갈림 이슈)

from collections import deque

def solution(n, infection, edges, k):
    # 1. 파이프별 그래프를 만들기 (각 파이프와 연결된 노드들 정보 정리)
    graphs = {
        1:[[] for _ in range(n+1)],
        2: [[] for _ in range(n+1)],
        3: [[] for _ in range(n+1)] }
    for i, j, p in edges:
        graphs[p][i].append(j)
        graphs[p][j].append(i)
    # 최종 정답
    max_result = 0
    # 2. k번해서 할 수 있는 모든 경우의 수 구하기
    # 2-1. dfs로 모든 경우의 수 해보고
    # 2-2. bfs로 감염된 것들 개수 세기
    def dfs(step, current_active_nodes):
        nonlocal max_result
        # dfs에서는 무조건 탈출 조건부터 넣기
        if step == k:
            max_result = max(max_result, len(current_active_nodes))
            return
        # 3가지 파이프(1, 2, 3) 중 하나를 고른다!
        for pipe_type in (1, 2, 3):
            # BFS 시작: 현재 활성화된 노드들을 전부 큐에 넣고 출발
            queue = deque(current_active_nodes)
            new_active_nodes = set(current_active_nodes) # 방문 처리 겸, 새로 활성화된 노드 모음 (중복 방지)
            
            while queue:
                curr = queue.popleft()
                # 내가 고른 파이프(pipe_type) 그래프만 타고 이동!
                for next_node in graphs[pipe_type][curr]:
                    if next_node not in new_active_nodes:
                        new_active_nodes.add(next_node)
                        queue.append(next_node)
            
            # 새로 활성화된 노드들(new_active_nodes)을 들고 다음 스텝(step + 1)
            dfs(step + 1, new_active_nodes)

    # 처음엔 infection 하나만 활성화된 상태(set)로 시작
    dfs(0, set([infection]))
    
    return max_result

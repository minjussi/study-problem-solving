# dfs와 bfs를 모두 사용하는 알고리즘
# 모든 경우의 수를 탐색 -> dfs
# k번 열어서 최대로 감염시키는 개수 세기 -> bfs(물론 dfs 해도 됨 but, 헷갈림 이슈)

from collections import deque

def solution(n, infection, edges, k):
    # 1. 파이프별 그래프를 만들기 (각 파이프와 연결된 노드들 정보 정리)
    graph = {
        1:[[] for _ in range(n+1)],
        2: [[] for _ in range(n+1)],
        3: [[] for _ in range(n+1)] }
    for i, j, p in edges:
        graph[p][i].append(j)
        graph[p][j].append(i)
    max_result = 0
    # 2. k번해서 할 수 있는 모든 경우의 수 구하기
    # 2-1. dfs로 모든 경우의 수 해보고
    # 2-2. bfs로 감염된 것들 개수 세기
    def dfs():

    return max_result

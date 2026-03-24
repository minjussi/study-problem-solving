def solution(n, infection, edges, k):
    answer = 0
    # 1. 파이프별 그래프를 만들기 (A와 연결된 노드들 정보 정리 등..)
    A = [[] for _ in range(n)]
    B = [[] for _ in range(n)]
    C = [[] for _ in range(n)]
    
    # 2. k번해서 할 수 있는 모든 경우의 수 구하기-> dfs 사용
    # 3. bfs로 연결된 거 찾아서 감염
    # 4. 감염된 거 infection에 넣기
    # infection 길이 반환
    return answer

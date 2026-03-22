# 상하좌우 움직임 조절법 무조건 숙지 !!
# 인덱스 에러 방지 nx, ny의 인덱스를 무조건 확인
# maps 자체에다가 지나온 길 숫자를 덮어쓰는 방식으로 진행할 것

from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)] # 파이썬 문법 기억
    # 무조건 특정 지점부터 시작 (네트워크 문제와의 차이점)
    queue = deque([(0, 0)])
    visited[0][0] = True
    # 파이썬에서 상하좌우 움직임에 사용되는 국룰 문법 !!
    dx = [-1, 1, 0, 0] # 상, 하
    dy = [0, 0, -1, 1] # 좌, 우
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m: # 인덱스 에러 방지. 무조건 확인 !!
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
                
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]
    

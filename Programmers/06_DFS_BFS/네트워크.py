from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            queue = deque([i])
            visited[i] = True
            
            while queue:
                current = queue.popleft()
                for neighbor in range(n):
                  # 
                    if current != neighbor and computers[current][neighbor] == 1 and not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
    return answer

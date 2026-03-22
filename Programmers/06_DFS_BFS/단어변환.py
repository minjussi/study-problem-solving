# 현재 단어, 지금까지 변환한 횟수 -> 튜플로 묶어서 횟수 표시 가능

from collections import deque

# 단어 비교하는 로직
def same_word(word1, word2):
    count = 0
    for c1, c2 in zip(word1, word2):
        if c1!= c2:
            count +=1
    return count

def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)]) # 단어, 지금까지 변환한 횟수
    visited = [False] * len(words)
    
    while queue:
        current_word, count = queue.popleft()
        if current_word == target:
            return count
            
        for i in range(len(words)):
            if not visited[i] and same_word(current_word, words[i]) == 1:
                visited[i] = True
                queue.append((words[i], count + 1)) 
                
    return 0

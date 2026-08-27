from collections import deque
def solution(cacheSize, cities):
    # 1. 예외처리 ,, (이런 것도 있구나)
    if cacheSize == 0:
        return len(cities) * 5
    answer = 0
    cache = deque()
    
    # 2. for 문을 돌면서 
    for city in cities:
        # 3. 소문자로 바꾸고
        city = city.lower()
        # 4. 캐시 히트 한 경우
        if city in cache:
            cache.remove(city) # 그 자리에 있는 걸 빼줘야 함 !!
            cache.append(city)
            answer += 1
        # 5. 캐시 미스인 경우
        else:
            if len(cache) >= cacheSize:
                cache.popleft()
            cache.append(city)
            answer += 5
            
    return answer

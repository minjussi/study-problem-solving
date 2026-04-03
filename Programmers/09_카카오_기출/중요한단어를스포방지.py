# 인덱싱을 정확히 하여서 조건을 만족하는 방법을 찾기
# 한 문제씩은 꼭 나오니 인덱싱 기법 숙지

def solution(message, spoiler_ranges):
    # 1. message에서 인덱스를 전부 추출한 문자열 만들기
    message_index = []
    start = 0
    for i in range(len(message)):
        if message[i] == " ":
            message_index.append([start, i-1])
            start = i+1
        if i == len(message)-1:
            message_index.append([start, i])   
    # 2. not_important_set - spoiler_ranges에 겹치는가? 안 겹치면 넣기
    not_important = []
    candidate = []
    for index in message_index:
        is_spoiler = False
        start = index[0]
        end = index[1]
        for spoiler in spoiler_ranges:
            if start <= spoiler[1] and spoiler[0] <= end:
                candidate.append(message[start:end+1])
                is_spoiler = True
        if not is_spoiler:
            not_important.append(message[start:end+1])
        
    # 3. not_important에 없고 candidate에서 중복x
    important = []
    for string in candidate:
        if string not in not_important:
            if string not in important:
                important.append(string)
    return len(important)

# 더 나은 코드
# set의 사용
# 겹치는 문자가 나오면 반복문 break

def solution(message, spoiler_ranges):
    message_index = []
    start = 0
    for i in range(len(message)):
        if message[i] == " ":
            message_index.append([start, i-1])
            start = i+1
        if i == len(message)-1:
            message_index.append([start, i])   
            
    # 1. 속도를 위해 리스트 대신 집합(set) 사용
    not_important = set() 
    candidate = []
    
    for index in message_index:
        is_spoiler = False
        start = index[0]
        end = index[1]
        for spoiler in spoiler_ranges:
            if start <= spoiler[1] and spoiler[0] <= end:
                candidate.append(message[start:end+1])
                is_spoiler = True
                break  # 2. 한 번이라도 겹치면 더 검사할 필요 없이 반복문 탈출!
                
        if not is_spoiler:
            not_important.add(message[start:end+1]) # 리스트의 append 대신 set의 add 사용
            
    important = set() # 여기서도 속도를 위해 집합 사용
    for string in candidate:
        if string not in not_important:
            important.add(string)
            
    return len(important)

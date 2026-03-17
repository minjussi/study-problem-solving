# 풀이 생각: 긴 변은 무조건 가로, 짧은 변은 무조건 세로로 보낸다
# 데이터가 10000(1만 개)이하면 그냥 무조건 다 경우의 수를 계산해본다

def solution(sizes):
    answer = 0
    for pair in sizes:
        if pair[0] < pair[1]:
            temp = pair[0]
            pair[0] = pair[1]
            pair[1] = temp
    max_w = 0
    max_h = 0
    for pair in sizes:
        if pair[0] > max_w:
            max_w = pair[0]
        if pair[1] > max_h:
            max_h = pair[1]
    answer = max_w * max_h
    return answer

# 다른 풀이1
def solution(sizes):
    for pair in sizes:
        if pair[0] < pair[1]:
            pair[0], pair[1] = pair[1], pair[0] # temp 없이 파이썬에서 가능한 방법

    max_w = 0
    max_h = 0
    for pair in sizes:
        if pair[0] > max_w:
            max_w = pair[0]
        if pair[1] > max_h:
            max_h = pair[1]
            
    return max_w * max_h

# 다른 풀이2
def solution(sizes):
    # 명함들(sizes)에서 각각 가로/세로 중 '큰 값'들만 모아서 그 중 max
    max_w = max([max(pair) for pair in sizes])
    
    # 명함들에서 각각 가로/세로 중 '작은 값'들만 모아서 그 중 max
    max_h = max([min(pair) for pair in sizes])
    
    return max_w * max_h

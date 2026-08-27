# 스택 안에 넣은 것: 시간의 흐름
# 

def solution(prices):
    answer = [0]* len(prices)
    stack = []
    for i in range(len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            past_time = stack.pop()
            answer[past_time] = i-past_time
        stack.append(i)
    while stack:
        past_time = stack.pop()
        answer[past_time] = len(prices)-1-past_time
    return answer

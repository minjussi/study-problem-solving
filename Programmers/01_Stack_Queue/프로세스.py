# 순서대로 처리해야 하는 문제는 큐를 사용 
# 이전 것과 비교를 해야하는 경우는 스택을 사용

def solution(priorities, location):
    answer = 0
    front = 0

    while True:
        max = True
        for i in range(len(priorities)):
            if priorities[front] < priorities[i]:
                max = False
                break
        if max:
            priorities[front] = -1
            answer += 1
            if front == location:
                return answer  
            
        front = (front + 1) % len(priorities)

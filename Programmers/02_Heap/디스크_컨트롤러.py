# 시간의 흐름을 일일이 따라가지 말고 그 다음 시간으로 바로 넘어가기
# 우선적으로 비교하고 싶은 요소를 제일 앞에 배치하여 튜플로 만들기

import heapq

def solution(jobs):
    jobs.sort(key=lambda x:x[0]) # 제일 처음 요청 시각을 기준으로 정렬
    answer = 0
    q = []
    time = 0
    i = 0
    complete = 0
    while complete != len(jobs):
        while i < len(jobs) and jobs[i][0] <= time: # 조건식도 잘 설정해야 함 -> 엣지 케이스 관리
            heapq.heappush(q, (jobs[i][1], jobs[i])) # 여기가 포인트 !
            i += 1
        if q: # 큐에 남은 작업이 있는지 확인
            run_p = heapq.heappop(q)[1]
            time += run_p[1]
            answer += time - run_p[0]
            complete += 1
        else: # 작업이 없으면 시간이 흐르도록 만들어 주기 
            time = jobs[i][0]
    return answer // len(jobs)        

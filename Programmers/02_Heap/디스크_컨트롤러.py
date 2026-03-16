import heapq

def solution(jobs):
    jobs.sort(key=lambda x:x[0])
    answer = 0
    q = []
    time = 0
    i = 0
    complete = 0
    while complete != len(jobs):
        while i < len(jobs) and jobs[i][0] <= time:
            heapq.heappush(q, (jobs[i][1], jobs[i]))
            i += 1
        if q:
            run_p = heapq.heappop(q)[1]
            time += run_p[1]
            answer += time - run_p[0]
            complete += 1
        else:
            time = jobs[i][0]
    return answer // len(jobs)        

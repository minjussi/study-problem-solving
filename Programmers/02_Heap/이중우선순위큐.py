# 힙은 최솟값만 보장함 (뒤에 순서는 보장하지 않음)
# 문제에서 사용한 방법: max 함수로 최댓값을 찾고, remove한 다음(힙의 규칙 어긴 값), heapify로 다시 정렬
import heapq

def solution(operations):
    answer = []
    q = []
    for i in range(len(operations)):
        op = operations[i].split()[0]
        value = int(operations[i].split()[1])
        if op == "D":
            if q:
                if value == 1: # 최댓값 제거하는 방법 !
                    max_val = max(q)
                    q.remove(max_val)
                    heapq.heapify(q)
                elif value == -1:
                    heapq.heappop(q)
        elif op == "I":
            heapq.heappush(q, value)
    if not q:
        answer = [0] * 2
    else:
        answer.append(max(q))
        answer.append(q[0])
    return answer

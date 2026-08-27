# DFS 문제: 재귀 함수를 사용한 풀이
# return 1, return 0: return add+sub를 하면 결국 모든 수를 더해지게 됨
# add, sub: 두 함수가 있으면 add를 실행하다가 -> return 0이 되면 그 지점에서 sub를 실행하는 것으로 넘어가게 됨
# (이런 식으로 깊이 탐색을 하게 되는 것임!!)

def solution(numbers, target):
    def dfs(index, cur_sum):
        if index == len(numbers):
            if cur_sum == target:
                return 1
            else:
                return 0
        add = dfs(index+1, cur_sum+numbers[index])
        sub = dfs(index+1, cur_sum-numbers[index])
        
        return add+sub
    
    return dfs(0, 0)

# 참고: return min(len(nums)//2, len(set(nums)))
# set의 사용: key만 중복 없이 모으는 함수
# 코드는 이대로 써도 무방 !

def solution(nums):
    answer = 0
    hash_dict = {}
    total = len(nums) // 2
    for i in nums:
        if answer >= total:
            return answer
        if i not in hash_dict:
            hash_dict[i] = 1
            answer += 1
    return answer

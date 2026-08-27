# 조합을 일일이 구할 필요는 없다.
# 각 카테고리에 +1(안 입는 선택지) 한 다음 전부 곱해서 마지막에 -1(전부 안 입는 선택지) 

def solution(clothes):
    answer = 1
    hash_dict = {}
    for cloth in clothes:
        if cloth[1] in hash_dict:
            hash_dict[cloth[1]] += 1
        else:
            hash_dict[cloth[1]] = 1
    for key, value in hash_dict.items():
        answer = answer * (value+1)
    return answer-1

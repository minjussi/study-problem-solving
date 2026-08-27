# 해시를 사용한 풀이
# 모든 값을 딕셔너리에 넣은 다음
# 첫 번째 값부터 하나씩 분해를 해서 -> 각 조각이 딕셔너리 안에 있는지 확인

def solution(phone_book):
    hash_dict={}
    for num in phone_book:
        hash_dict[num] = 1
    for phone_num in phone_book:
        temp = ""
        for num in phone_num: # 이중for문이지만, 길이가 20자를 넘지 않기 때문에 효율성도 통과 !!!
            temp += num
            if temp in hash_dict and temp != phone_num:
                return False
    return True

# 해시가 아닌 다른 풀이
def solution(phone_book):
    # 사전식으로 정렬 -> 앞자리를 기준으로 1부터 정렬하게 됨
    phone_book.sort()
    
    # 내 번호랑 '바로 뒷번호' 딱 2개만 비교하면서 지나가기
    for i in range(len(phone_book) - 1):
        # 뒷번호가 내 번호로 시작하면 접두어이므로 false 반환
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True

# after: 해시를(딕셔너리) 사용한 풀이
# 딕셔너리는 key, value 쌍으로 데이터를 저장함 (딕셔너리 이름['key']=value로 값을 저장함)

def solution(participant, completion):
    hash_dict = {}
    
    # 1. 참가자 명단 만들기
    for p in participant:
        if p in hash_dict:
            hash_dict[p] += 1 # 동명이인이 있으면 숫자 추가
        else:
            hash_dict[p] = 1  # 처음 등장하면 1명 등록
            
    # 2. 완주자 명단 보면서 참가자 명단에서 지우기
    for c in completion:
        hash_dict[c] -= 1
        
    # 3. 마지막에 출석부에 1로 남아있는 한 명이 완주하지 못한 선수
    for key, value in hash_dict.items():
        if value == 1:
            return key


# before: 이중 for문을 사용하면 효율성이 박살남
def solution(participant, completion):
    answer = ''
    for complete in completion:
        for name in participant:
            if complete == name:
                participant.remove(name)
                break
    answer ="".join(participant)
    return answer

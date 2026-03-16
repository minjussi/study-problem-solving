#after


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

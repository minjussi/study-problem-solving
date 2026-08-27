def solution(k, tangerine):
    # 서로 다른 종류가 최소가 되는 경우의 종류의 수
    answer = 0
    # 1. 크기가 같은 것이 몇 번 나오는지 기록
    size_dict = {}
    for size in tangerine:
        if size in size_dict:
            size_dict[size] += 1
        else:
            size_dict[size] = 1
    # 2. 많이 나온 순서대로 정렬
    # x[0] : key, x[1] : value
    sorted_dict = sorted(size_dict.items(), key=lambda x: -x[1])
    # 3. value 값만큼 k에서 빼면서 k=0이 되는 시점 종류의 수 return
    for key, value in sorted_dict:
        answer += 1
        k -= value
        if k<=0:
            break
    return answer

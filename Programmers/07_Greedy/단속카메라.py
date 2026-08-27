def solution(routes):
    answer = 0
    # 1. 나간 시점을 기준으로 정렬하기 !! (이 부분에 유의) 
    # 나간 시점을 기준으로 정렬해야 겹칠 확률이 높아지는 것이지요
    routes.sort(key=lambda x:x[1])
    # 2. 나간 시점을 기준 삼음 (나머지 로직은 다 맞음)
    # 최솟값은 float('-inf')
    camera = float('-inf')
    for route in routes:
        # 3. 나간 시점이 다음 진입시점보다 작으면 그 위치의 나간시점에 다시 카메라 설치
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer

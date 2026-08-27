# sorted를 무조건 해 줄 것
# 앞번호부터 차례대로 빌려줘야 로직이 정상적으로 돌아감
# 차집합 사용하여 real_lost와 real_reserve 다시 계산해야 함(문제 조건)

def solution(n, lost, reserve):
    real_lost = set(lost)-set(reserve)
    real_reserve = set(reserve)-set(lost)
    for num in sorted(real_reserve):
        if (num-1) in real_lost:
            real_lost.remove(num-1)
        elif (num+1) in real_lost:
            real_lost.remove(num+1)
    return n-len(real_lost)

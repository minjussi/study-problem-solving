# permutations를 활용하는 방법
# 소수를 판별하는 방법
from itertools import permutations

def solution(numbers):
    answer = 0
    # 만들 수 있는 숫자 다 만들기
    prime_set = set()
    
    for length in range(1, len(numbers)+1):
        for piece in permutations(numbers, length):
            string = "".join(piece)
            prime_set.add(int(string))
    # 소수 판별
    for num in prime_set:
        is_prime = True
        if num <= 1:
            is_prime = False
        i = 2
        while i*i <= num:
            if num % i == 0:
                is_prime = False
            i += 1  
        if is_prime:
            answer += 1
    return answer

# 다양한 코드들에 대한 공부
# 소수를 판별하는 방법 - 파이썬 스타일
for i in range(2, int(num**0.5) + 1): # **0.5로 루트 씌우고 int로 소수점 제거
    if num % i == 0:
        is_prime = False
        break

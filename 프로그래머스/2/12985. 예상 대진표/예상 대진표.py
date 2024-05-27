import math
def solution(n,a,b):
    answer = 0
    #반씩 줄어ㅓ든다.
    while a != b:
        a, b = math.ceil(a / 2), math.ceil(b / 2)
        answer += 1

        
    return answer
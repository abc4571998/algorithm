from itertools import permutations 
import math
def solution(n):
    # 2가 최대 들어갈 개수
    max_count_of_two = n // 2
    print(max_count_of_two)
    # 2를 0개에서 하나씩 늘려가본다. 그에 해당하는 조합을 만든다.
    answer = 0
    # 피보나치
    if n == 1: 
        return 1
    elif n == 2:
        return 2
    else: 
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    
    return dp[-1]
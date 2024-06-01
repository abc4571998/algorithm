from itertools import permutations 
import math
def solution(n):
    # 팩토리얼로 진행했다가 피보나치로 변경
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

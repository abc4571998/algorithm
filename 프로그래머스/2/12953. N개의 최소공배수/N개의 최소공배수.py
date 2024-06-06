def gcd(a, b):
    for i in range(min(a,b), 0, -1):
        if a%i == 0 and b%i == 0:
            return i
    return 1

def solution(arr):
    answer = 1
	# 최대공약수 구하기
    for i in arr:
        #최소공배수를 구하고 계속 곱해준다
        answer = (answer*i) // gcd(answer, i)
    return answer
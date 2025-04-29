count = 0

def solution(nums):
    dfs(nums, 0, [])
    return count

def isPrime(num):
    result = 0
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def dfs(arr, i, current):
    global count
    if len(current) == 3:
        if isPrime(sum(current)):
            count += 1
        return
    if i >= len(arr):
        return
    dfs(arr, i+1, current + [arr[i]])
    dfs(arr, i+1, current)
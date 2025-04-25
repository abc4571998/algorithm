n, s = map(int, input().split())
numbers = list(map(int, input().split()))

result = 0
def dfs(sum, numbers, i):
    global result
    if sum + numbers[i] == s:
        result += 1
    if i == n - 1:
        return
    dfs(sum, numbers, i+1)
    dfs(sum + numbers[i], numbers, i+1)

dfs(0, numbers, 0)
print(result)
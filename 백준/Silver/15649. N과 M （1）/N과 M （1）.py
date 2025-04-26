n, m = map(int, input().split())
# 1부터 n까지에서 길이가 m 인 수열 (중복 x)

def dfs(current, visited):
    if len(current) == m:
        print(" ".join(map(str, current)))
        return
    
    for i in range(1, n+1):
        if i not in visited:
            visited.add(i)
            dfs(current + [i], visited)
            visited.remove(i)
dfs([], set())
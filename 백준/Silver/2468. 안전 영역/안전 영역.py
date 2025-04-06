n = int(input())
max_num = 0
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))
    for j in range(n):
        if max_num < graph[i][j]:
            max_num = graph[i][j]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def dfs(x, y, height, visited):
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] > height:
                    visited[nx][ny] = True
                    stack.append((nx, ny))

result = 0
for k in range(max_num):
    visited = [[False]*n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and not visited[i][j]:
                dfs(i, j, k, visited)
                cnt += 1
    if result < cnt:
        result = cnt

print(result)


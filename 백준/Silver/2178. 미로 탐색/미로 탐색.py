from collections import deque

n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input())))

def bfs(arr, x, y):
    queue = deque([(x, y)])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue: 
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx, ny))

bfs(arr, 0, 0)
print(arr[n-1][m-1])
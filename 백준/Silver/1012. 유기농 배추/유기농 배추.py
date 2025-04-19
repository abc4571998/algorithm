from collections import deque
t = int(input())

def bfs(i, j, arr):
    queue = deque([(i, j)])
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while(queue):
        x, y = queue.pop()
        arr[x][y]  = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and arr[nx][ny]:
                queue.append((nx, ny))


for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0] * n for _ in range(m)]
    for i in range(k):
        x, y = map(int, input().split())
        arr[x][y] = 1
    count = 0
    for v in range(m):
        for w in range(n):
            if arr[v][w] == 1:
                bfs(v, w, arr)
                count += 1
    print(count)
    

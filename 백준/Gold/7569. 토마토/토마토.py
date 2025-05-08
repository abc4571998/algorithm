from collections import deque

# M: 가로칸, N: 세로칸, H: 높이
m, n, h = map(int, input().split())

arr = []
tomato_place = []

for k in range(h):
    arr.append([])
    for i in range(n):
        row = list(map(int, input().split()))
        arr[k].append(row)
        for j in range(len(row)):
            if row[j] == 1:
                tomato_place.append((i, j, k))
    

#1은 익은 토마토, 0은 익지 않은 토마토, -1은 빈칸
#처음부터 모두 익어있으면 0, 모두 익지 못하면 -1

def bfs(arr, start, m, n, h):
    queue = deque(start)

    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    while queue:
        x, y, z = queue.popleft()
        for t in range(6):
            nx = x + dx[t]
            ny = y + dy[t]
            nz = z + dz[t]
            
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if arr[nz][nx][ny] == 0:
                    arr[nz][nx][ny] = arr[z][x][y] + 1
                    queue.append((nx, ny, nz))
        
bfs(arr, tomato_place, m, n, h)

max_day = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if arr[z][x][y] == 0:  # 아직도 안익은 토마토가 있다면
                print(-1)
                exit(0)
            max_day = max(max_day, arr[z][x][y])

print(max_day - 1)
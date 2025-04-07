n, m = map(int, input().split())
r, c, d = map(int, input().split())

arr = [[] for _ in range(n)]
for i in range(n):
    arr[i]= list(map(int, input().split()))

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

cleaned = 1

def dfs(x, y, dist):
    global cleaned
    #청소하기
    arr[x][y] = 2
    #주변칸을 본다

    for i in range(4):
        #90도 돌았는데 바라보는 칸이 0이면 전진하고 청소
        dist -= 1
        if dist < 0:
            dist = 3
        nx = x + dx[dist]
        ny = y + dy[dist]

        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
            cleaned += 1
            dfs(nx, ny, dist)
            return
        
    bx = x - dx[dist]
    by = y - dy[dist]
    if 0 <= bx < n and 0 <= by < m and arr[bx][by] != 1:
        dfs(bx, by, dist)  # 후진해서 다시 시도
    else:
        return  # 뒤도 벽이면 종료

dfs(r, c, d)

print(cleaned)
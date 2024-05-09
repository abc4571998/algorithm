from collections import deque

def bfs(maps):
    n = len(maps)
    m = len(maps[0])
    #visited = [[False for _ in range(m)] for _ in range(n)]
    queue = deque([(0,0)])
    maps[0][0] = 2
    #1. 상하좌우로 이동한다.
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        #visited[x][y] = True
        if (x == n-1 and y == m-1):
            #print('find ', maps[x][y])
            return maps[x][y] -1
        #print(node, x, y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1) :
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
                    #print(queue)
                    
                    
    return -1

def solution(maps):
    answer = bfs(maps)
    return answer
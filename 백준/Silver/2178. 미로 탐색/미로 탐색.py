from collections import deque

flame = []
n, m = map(int, input().split())
for _ in range(n):
  flame.append([int(x) for x in input()])
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, x, y):
  queue = deque()
  queue.append((x, y))
  while queue:
      x, y = queue.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 0:
          continue
        if graph[nx][ny] == 1:
          graph[nx][ny] = graph[x][y] + 1
          queue.append((nx, ny))
  return graph[n-1][m-1]

print(bfs(flame, 0, 0))


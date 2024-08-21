
from collections import deque

def bfs(maps, starts):
    queue = deque([(i, j, 1) for i, j in starts])
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        x, y , days = queue.popleft()
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != -1:
                if maps[nx][ny] == 0 or maps[nx][ny] > days + 1:
                    queue.append((nx,ny, days +1))
                    maps[nx][ny] = days+1


cols, rows = map(int, input().split())
maps = []
starts = []
for i in range(rows):
    row = list(map(int, input().split()))
    maps.append(row)
    for j in range(cols):
        if row[j] == 1:
            starts.append((i, j))

bfs(maps, starts)

max_num = 0
for row in maps:
    if 0 in row:
        max_num = 0
        break
    max_num = max(max(row), max_num)
print(max_num-1)
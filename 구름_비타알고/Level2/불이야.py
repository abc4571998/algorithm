from collections import deque

def bfs_fire(maps, fires):
	n, m = len(maps), len(maps[0])
	fire_time = [[float('inf')] * m for _ in range(n)]  # 불이 퍼지는 시간
	queue = deque([(x, y, 0) for x, y in fires])

	for x, y in fires:
		fire_time[x][y] = 0
		
	moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

	while queue:
			x, y, time = queue.popleft()
			for dx, dy in moves:
					nx, ny = x + dx, y + dy
					if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != '#' and fire_time[nx][ny] == float('inf'):
							fire_time[nx][ny] = time + 1
							queue.append((nx, ny, time + 1))

	return fire_time

n, m = map(int, input().split())
maps = []
fires = []
my_place = None

for row in range(n):
	cols = list(input())
	maps.append(cols)
	for col, item in enumerate(cols):
			if item == '@':
					fires.append((row, col))
			elif item == '&':
					my_place = (row, col)

fire_time = bfs_fire(maps, fires)

# 내 위치까지의 최소 시간을 계산
answer = fire_time[my_place[0]][my_place[1]]

if answer == float('inf'):
	print(-1)
else:
	print(answer - 1)

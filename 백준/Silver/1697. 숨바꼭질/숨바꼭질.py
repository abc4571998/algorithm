from collections import deque

start, target = map(int, input().split())


MAX = 10 ** 5
visited = [0] * (MAX+1)

def bfs(start):
    queue = deque([start])
    while queue:
        s = queue.popleft()
        if s == target:
            return visited[s]
        for i in (s-1, s+1, s*2):
            if 0 <= i <= MAX and not visited[i]:
                visited[i] = visited[s] + 1
                queue.append(i)

print(bfs(start))
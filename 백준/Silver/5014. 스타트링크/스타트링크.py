from collections import deque

f, s, g, u, d = map(int, input().split())
visited = [0] * (f+1)

def bfs(start):
    queue = deque([start])
    visited[start] = 1

    while queue:
        floor = queue.popleft()
        if floor == g:
            return visited[floor]
        
        for i in (floor + u, floor - d):
            if 1 <= i <= f and not visited[i]:
                visited[i] = visited[floor] + 1
                queue.append(i)
    return None

result = bfs(s)
if result is None:
    print("use the stairs")
else:
    print(result-1)

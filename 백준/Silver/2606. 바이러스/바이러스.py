from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    queue = deque([start])
    visited = set({start})
    result = 0
    while queue:
        node = queue.popleft()
        for item in graph[node]:
            if item in visited:
                continue
            else:
                visited.add(item)
                result += 1
                queue.append(item)
    return result

print(bfs(1))
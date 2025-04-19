from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
nodes = [[] for _ in range(n)]

def bfs(source, nodes, visited):
    queue = deque([source])
    visited[source] = True

    while queue:
        start = queue.popleft()
        link_nodes = nodes[start]
        for i in range(len(link_nodes)):
            target = link_nodes[i]
            if not visited[target]:
                visited[target] = True
                queue.append(target)

for _ in range(m):
    source, target = map(int, input().split())
    nodes[source-1].append(target-1)
    nodes[target-1].append(source-1)

visited = [False]*n
count = 0
for i in range(n):
    if not visited[i]:
        bfs(i, nodes, visited)
        count += 1

print(count)
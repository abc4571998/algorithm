from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    node, edge = map(int, input().split())
    graph[node].append(edge)
    graph[edge].append(node)

dfs_answer = []
def dfs(target, visited):
    #해당 노드에 연결되어있는 노드들 가져오기
    #노드 방문했다면 패스, 아니라면 스택에 넣기 
    nodes = graph[target]
    dfs_answer.append(str(target))
    for item in sorted(nodes):
        if item in visited:
            continue
        else:
            visited.add(item)
            dfs(item, visited)
        

dfs(v, set({v}))
print(" ".join(dfs_answer))

bfs_answer = []
visited = set()
def bfs(start):
    #인접한 노드들 큐에 넣고 돌리기 
    queue = deque([])
    visited.add(start)
    queue.append(start)
    while queue:
        item = queue.popleft()
        bfs_answer.append(str(item))
        for i in sorted(graph[item]):
            if i in visited:
                continue
            else:
                visited.add(i)
                queue.append(i)
        

bfs(v)
print(" ".join(bfs_answer))
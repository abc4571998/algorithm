n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

answer = []

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(start, target, visited, result):
    if start == target:
        return result
    node = graph[start]
    for item in node:
        if item not in visited:
            visited.add(item)
            res = dfs(item, target, visited, result+1)
            if res is not None:
                return res
    return None

res = dfs(p1, p2, set({p1}), 0)
print(res if res is not None else -1)
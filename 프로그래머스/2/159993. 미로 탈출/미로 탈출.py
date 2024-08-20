from collections import deque

def bfs(graph, start, end):
    visited = [[False]* len(graph[0]) for _ in range(len(graph))]
    queue = deque([(start[0], start[1], 0)])
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        x,y, count = queue.popleft()
        if (x,y) == end:
            return count
        for move in moves:
            dx, dy = x + move[0], y + move[1]
            if 0 <= dx < len(graph) and 0 <= dy < len(graph[0]) and not visited[dx][dy] and graph[dx][dy] != 'X':
                visited[dx][dy] = True
                queue.append((dx, dy, count + 1))

    return -1
    
def solution(maps):
    answer = 0
    start = tuple()
    lever = tuple()
    end = tuple()
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start=(i,j)
            elif maps[i][j] == 'L':
                lever=(i,j)
            elif maps[i][j] == 'E':
                end=(i,j)
                
    count_lever = bfs(maps, start, lever)
    if count_lever == -1:
        return -1
    
    count_end = bfs(maps, lever, end)
    if count_end == -1:
        return -1
    else:
        return count_lever+count_end
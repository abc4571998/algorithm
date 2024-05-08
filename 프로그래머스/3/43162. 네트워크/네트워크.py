from collections import deque

def bfs(computers, visited, start):
    queue = deque([(start, computers[start])])
    
    count = 0
    #0. 큐에서 꺼내서 연결된 노드를 확인한다.
    while queue:
        node, neighbors = queue.popleft()
        #print(node, neighbors)
        visited[node] = True
        for i in range(len(neighbors)):
    		#1. 연결된 네트워크를 큐에 넣는다. 방문한 노드는 안된다.
            if(visited[i] == False and neighbors[i] == 1):
                queue.append((i, computers[i]))
                #print('queue ', queue)


def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for i in range(n):
        if visited[i] == False:
            bfs(computers, visited, i)
            answer += 1
            #print(answer)
         	
    return answer
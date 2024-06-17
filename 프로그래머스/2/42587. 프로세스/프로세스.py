from collections import deque
def solution(priorities, location):
    answer = 0
    first_process = priorities.index(max(priorities))
    if first_process == location : return 1

    queue = deque([{'priority': priorities[i], 'index': i} for i in range(len(priorities))])
    sorted_priorities = sorted(priorities)
    
    count = 0
    while(queue):
        process = queue.popleft()
        max_priority = sorted_priorities[-1]
        if process['priority'] == max_priority:
            count += 1
            sorted_priorities.pop()
            if location == process['index']:
                return count
        else:
            queue.append(process)
            
    return len(priorities)
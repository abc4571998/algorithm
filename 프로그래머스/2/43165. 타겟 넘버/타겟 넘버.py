from collections import deque 

def bfs(numbers, target):
    queue = deque([])
    # 1. 부호는 두가지 경우 +, -
    queue.append(int(numbers[0]))
    queue.append(int(numbers[0])*(-1))
    # 2. 현재 값에 +, - 한 값을 더해서 넘긴다.
    
    
    for i in range(1, len(numbers)): 
        length = len(queue)
        for _ in range(length):
	        num = queue.popleft()
        	queue.append(num + int(numbers[i]))
        	queue.append(num + int(numbers[i])*(-1))
            
    target_count = [x for x in queue if x == target]
    return len(target_count)
        
def solution(numbers, target):
    answer = bfs(numbers, target)
    return answer
from collections import deque

num = int(input())
queue = deque([])
answer = []
for _ in range(num):
    line = input().split()
    cmd = line[0]
    if cmd == 'push_front': queue.appendleft(line[1])
    elif cmd == 'push_back': queue.append(line[1])
    elif cmd == 'pop_front': 
        if queue: answer.append(queue.popleft())
        else: answer.append(-1)
    elif cmd == 'pop_back': 
        if queue: answer.append(queue.pop())
        else: answer.append(-1)
    elif cmd == 'size': answer.append(len(queue))
    elif cmd == 'empty': 
        if not queue: answer.append(1)
        else: answer.append(0)
    elif cmd == 'front': 
        if queue: answer.append(queue[0])
        else: answer.append(-1)
    elif cmd == 'back': 
        if queue: answer.append(queue[-1])
        else: answer.append(-1)

    
for item in answer:
    print(item)

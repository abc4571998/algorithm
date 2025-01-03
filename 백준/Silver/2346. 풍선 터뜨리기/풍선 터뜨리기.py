import sys
from collections import deque

n = int(sys.stdin.readline())
numbers = sys.stdin.readline().split()

queue = deque([])
for i in range(n):
    queue.append((int(numbers[i]), i+1))

count = 1
index = 1
for _ in range(n):
    num = 0
    if count > 0:
        for i in range(count):
            num, idx = queue.popleft()
            if i != count-1:
                queue.append((num, idx))
    else:
        count = count*(-1)
        for i in range(count):
            num, idx = queue.pop()
            if i != count-1:
                queue.appendleft((num, idx))
    count, index  = num, idx
    print(index, end=' ')


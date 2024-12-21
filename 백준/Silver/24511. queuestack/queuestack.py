import sys
from collections import deque

n = int(sys.stdin.readline())

type = list(map(int, sys.stdin.readline().split()))
stack = []
queue = deque([])

numbers = list(map(int, sys.stdin.readline().split()))
count = int(sys.stdin.readline())
values = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    if type[i] == 0:
        queue.append(numbers[i])

for value in values:
    queue.appendleft(value)
    print(queue.pop(), end=' ')
import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque(map(int, sys.stdin.readline().split()))
stack = []

turn = 1


while queue:
    current = queue.popleft()
    stack.append(current)
    while stack and stack[-1] == turn:
        stack.pop()
        turn += 1

if stack:
    print("Sad")
else:
    print("Nice")
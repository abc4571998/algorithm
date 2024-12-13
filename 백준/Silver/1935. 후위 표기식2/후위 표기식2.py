import sys
from collections import deque

n = int(sys.stdin.readline())

eval = sys.stdin.readline().strip()

stack = []

alpha_dict = {}
start = 65
for _ in range(n):
    alpha_dict[chr(start)] = float(sys.stdin.readline())
    start += 1
    
for value in eval :
    if value.isalpha():
        stack.append(alpha_dict[value])
    else:
        second = stack.pop()
        first = stack.pop()
        result = 0
        if value == '+':
            result = first+second
        elif value == '-':
            result = first-second
        elif value == '/':
            result = first/second
        elif value == '*':
            result = first*second
        stack.append(result)

print('%.2f'%stack.pop())
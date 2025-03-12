from collections import deque

#2를 곱하거나 1을 붙이기
start, target = map(int, input().split())

queue = deque([(start,1)])
result = -1
while queue:
    num, cnt = queue.popleft()
    if num == target:
        result = cnt
        break
    if num*2 <= target:
        queue.append((num*2, cnt+1))
    if int(str(num)+'1') <= target:
        queue.append((int(str(num)+'1'), cnt+1))

print(result)

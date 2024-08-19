from collections import deque
card_count = int(input())
card_nums = [i+1 for i in range(card_count)]
queue = deque(card_nums)
while len(queue) != 1:
    queue.popleft()
    queue.rotate(-1)

print(queue[0])
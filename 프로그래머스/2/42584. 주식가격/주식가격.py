from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        price = queue.popleft()
        count = 0
        for next_price in queue:
            count += 1
            if price > next_price:
                break
        answer.append(count)
        
        
    return answer
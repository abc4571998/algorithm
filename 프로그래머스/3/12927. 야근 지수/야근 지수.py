import heapq

def solution(n, works):
    #최대한 낮은 수가 되도록 큰수부터 하나씩 빼준다.
    max_heap = [-x for x in works]
    heapq.heapify(max_heap)
    if sum(works) <= n:
        return 0
    for _ in range(n):
        max_value = heapq.heappop(max_heap)
        heapq.heappush(max_heap, max_value+1)
        
    answer = sum(x**2 for x in max_heap)
    return answer
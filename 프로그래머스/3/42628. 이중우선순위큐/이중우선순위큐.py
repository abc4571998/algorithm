import heapq
def solution(operations):
    min_heap = []
    max_heap = []
    for operation in operations:
        command, value = operation.split();
        value = int(value)
        if command == 'I': 
            heapq.heappush(min_heap, value)
            heapq.heappush(max_heap, -value)
        elif value == -1 and min_heap:
            min_value = heapq.heappop(min_heap)
            max_heap.remove(-min_value)
            heapq.heapify(max_heap)
        elif value == 1 and max_heap:
            max_value = -heapq.heappop(max_heap)
            min_heap.remove(max_value)
            heapq.heapify(min_heap)
    
    if len(min_heap) > 0:
        min_value = heapq.heappop(min_heap)
        max_value = -heapq.heappop(max_heap)
        return [max_value, min_value]
    return [0,0]
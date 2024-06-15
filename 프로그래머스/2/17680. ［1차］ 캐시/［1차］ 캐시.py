from collections import deque
def solution(cacheSize, cities):
    answer = 0
    # 캐시 교체 알고리즘은 LRU 
    # 캐시 크기만큼 도시 이름을 가지고 있음
    # 도시가 캐시에 있다면 hit, 실행시간 1
    # 도시가 캐시에 없다면 miss, 실행시간 5, 캐시가 넘치면 오래된 것 빼고 새로 넣기
    queue = deque([])
    if cacheSize == 0:
        return len(cities)*5
    for city in cities:
        city = city.lower()
        if city in queue:
            answer += 1
            queue.remove(city)
            queue.append(city)
        else:
            if len(queue) >= cacheSize:
            	queue.popleft()
            queue.append(city)
            answer += 5

    return answer
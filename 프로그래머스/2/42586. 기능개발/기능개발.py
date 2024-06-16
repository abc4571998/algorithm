import math
from collections import Counter
def solution(progresses, speeds):
    # 뒤에 있는 기능이 앞 기능보다 먼저 개발될 수 있음
    # 뒷 기능은 앞 기능 배포될 때 함께 배포
    # progresses 는 배포순으로 작업 진도를 나타냄
    
    # 1. 각 프로세스마다 며칠 후에 배포할 수 있는지 계산한다.
    dic= {}
    distribution_days = []
    front_distribution = 0
    for i in range(len(progresses)):
        progress = progresses[i]
        speed = speeds[i]
        remaining_progress = 100 - progress # 남은 작업 진도
        distribution_day = math.ceil(remaining_progress / speed) # 배포 가능한 날짜 (며칠 후)
        # 2. 앞 작업이 배포될때 뒷 작업도 같이 배포될 수 있음
        # 앞 작업보다 더 오래걸리는 배포 날짜는 그 날짜로 배포
        if distribution_day >= front_distribution:
            front_distribution = distribution_day
        # 앞 작업보다 빨리 배포될 수 있어도 후에 배포
        distribution_days.append(front_distribution)		
    answer = list(Counter(distribution_days).values())
    
    
    
    return answer
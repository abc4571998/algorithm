import re
def solution(s):
    answer = []
    tuples = re.findall(r'{([\d,]+)}', s)
    list_s = [list(map(int, x.split(','))) for x in tuples]
    list_s.sort(key=len)
    
    seen = set()
    # 각 리스트에서 이전에 보지 않은 숫자들만 추출
    for sublist in list_s:
        for num in sublist:
            if num not in seen:
                answer.append(num)
                seen.add(num)
                
    return answer
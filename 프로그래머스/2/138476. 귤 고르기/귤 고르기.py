from collections import Counter
def solution(k, tangerine):
    result = 0
    # count 를 확인하고, 가장 큰 값부터 빼간다.
    counter = Counter(tangerine).most_common()
    for element in counter:
        value = element[1]
        if(k > 0):
            k -= value
            result += 1
    return result
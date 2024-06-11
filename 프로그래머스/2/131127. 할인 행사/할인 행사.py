from collections import Counter

def solution(want, number, discount):
    want_dict = {want[i]: number[i] for i in range(len(want))}
    answer = 0
    for i in range(len(discount) - 9):
		# 조건을 만족하는 개수
        current_window = Counter(discount[i:i+10])
        if current_window == want_dict:
            answer += 1  
    return answer
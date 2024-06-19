from itertools import product

def solution(clothes):
    # clothes 를 딕셔너리로 만들기
    clothes_category = {x[1]: set() for x in clothes}
    for cloth in clothes:
        clothes_category[cloth[1]].add(cloth[0])
    
	# 종류당 하나만 선택할 수 있음
    all_combinations = 1
    for items in clothes_category.values():
        all_combinations *= (len(items) + 1)
        
    return all_combinations - 1
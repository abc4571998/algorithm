from collections import Counter

def solution(topping):
    answer = 0
    # 처음에 철수가 다 가지고 있고 동생한테 하나씩 줘보기
    cheolsoo = Counter(topping)
    brother = set()

    for item in topping:
        cheolsoo[item] -= 1
        brother.add(item)
        if cheolsoo[item] == 0:
            cheolsoo.pop(item)
        if len(cheolsoo) == len(brother):
            answer += 1
            
    return answer
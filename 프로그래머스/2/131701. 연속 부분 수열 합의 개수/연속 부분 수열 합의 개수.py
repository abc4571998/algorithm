def solution(elements):
    answer = set()
    # 배열 길이를 최대 길이로 합을 구할 수 있다.
    # 기본적으로 중복을 피하기 위해 set 으로 계산하기
    for i in range(1, len(elements)+1):
        arr = [sum(elements[x:x+i]) if x+i <= len(elements) else sum(elements[x:] + elements[0: x+i-len(elements)]) for x in range(len(elements))]
        answer.update(arr)
    return len(answer)
def solution(arr):
    answer = []
    
    # 1. 이전 숫자 저장하는 변수 하나 만들기
    prev = None;
    for item in arr:
        # 2. 이전 값과 다르다면 정답 배열에 추가
        if prev != item:
            prev = item;
            answer.append(item);
    return answer
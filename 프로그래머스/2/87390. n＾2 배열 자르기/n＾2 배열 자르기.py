def solution(n, left, right):
    # 2차원 배열 만들지 말고 계산해보기 
    # n 3, left 2, right 5 이면 2는 0행 2열, 5는 1행 2열임
    # left // n 행, left%n 열
    answer = []
    for i in range(left, right+1):
        row = i // n
        col = i % n
        answer.append(max(row,col)+1)         
    return answer
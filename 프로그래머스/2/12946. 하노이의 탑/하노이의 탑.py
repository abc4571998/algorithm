def hanoi(start, end, middle, answer, n):
    if n == 1:
        answer.append([start, end])
    else:      
        hanoi(start, middle, end, answer, n-1)
        answer.append([start, end])
        hanoi(middle, end, start, answer, n-1)
        
def solution(n):
    answer = []
    hanoi(1, 3, 2, answer, n)
        
    return answer
def count_bar(parentheses):
    stack = []   
    prev = None 
    answer = 0
    for item in parentheses:
        current = item
        if current == ')':
            stack.pop()
            if prev == '(':
                answer += len(stack)
            else:
                answer += 1
        else:
            stack.append(current)
        prev = current
    return answer
        
n = int(input())
for i in range(n):
    parentheses = input()
    #출력 형식
    print(f"#{i+1} {count_bar(parentheses)}")
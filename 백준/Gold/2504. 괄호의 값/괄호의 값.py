brackets = dict({')': '(', ']': '['})
bracket_weight = dict({')': 2, ']': 3, '(': 2, '[': 3})
expression = input()

stack = []
num = 1
answer = 0
prev = None

for exp in expression:
    #1. 왼쪽 괄호면 스택에 추가
    if exp in brackets.values():
        stack.append(exp)
        num *= bracket_weight[exp]
    #2. 오른쪽 괄호가 나오면 스택에서 빼기
    elif exp in brackets:
        if not stack:
            answer = 0
            break
        else: 
            pop_value = stack.pop()
            if pop_value == brackets[exp]:
                if prev == pop_value:
                    answer += num 
                num //= bracket_weight[exp]
            else: 
                answer = 0
                break
    
    prev = exp

if stack:
    print(0)        
else: print(answer)
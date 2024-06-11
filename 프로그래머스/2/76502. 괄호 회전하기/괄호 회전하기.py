from collections import deque
def check_brackets(s):
    #주어진 문자열이 괄호짝이 맞는지 확인
    bracket_map = {')': '(', '}': '{', ']': '['}
    open_brackets = set(bracket_map.values())
    stack = []
    for char in s:
        if char in open_brackets:
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack.pop() != bracket_map[char]:
                return False
    return len(stack) == 0

def solution(s):
    answer = 0
    deq = deque(s)
    for i in range(len(s)):
        if(check_brackets(deq)):
            answer += 1
       	deq.append(deq.popleft())
        
    return answer
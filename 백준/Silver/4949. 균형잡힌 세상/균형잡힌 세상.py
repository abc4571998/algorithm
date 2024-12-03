import re

while True:
    s = input()
    if s == '.':
         break
    brackets = re.sub(r"[a-zA-Z .]", "", s)
    stack = []
    pairs = {')': '(', ']' : '['}
    answer = True
    for bracket in brackets:
        if bracket not in pairs:
            stack.append(bracket)
        elif not stack or stack.pop() != pairs[bracket]:
            answer = False
            break
    
    if stack or not answer:
        print('no')
    else:
        print('yes')
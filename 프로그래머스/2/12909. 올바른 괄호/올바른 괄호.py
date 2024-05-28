def solution(s):
    stack = []
    #) 가 나오면 pop 했을때 ( 가 있어야 한다.
    for bracket in s:
        if bracket == "(":
            stack.append(bracket)
        else:
            if not stack or stack.pop() != "(":
                return False

    if stack: return False
    return True
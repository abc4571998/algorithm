import sys

pipes = list(sys.stdin.readline().strip())
stack = []
prev = ''
answer = 0

for pipe in pipes:
    #파이프가 ( 이면 스택에 넣기
    if pipe == '(':
        stack.append('(')
    else:
        stack.pop()
        #이전 파이프가 ( 라면 스택 개수만큼 카운트
        if prev == '(':
            answer += len(stack)
        #이전 파이프가 ) 이면 개수 하나만 더 세기
        else:
            answer += 1
    prev = pipe

print(answer)
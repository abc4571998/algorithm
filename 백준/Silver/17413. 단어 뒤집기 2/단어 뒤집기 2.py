import sys

sentence = sys.stdin.readline().strip()

stack = []

prev = ''

for alpha in sentence:
    # < 면 > 가 나올때까지 출력
    if alpha == '>':
        print(alpha, end='')
        prev = '>'
    elif alpha == '<' or prev == '<':
        while stack:
            print(stack.pop(), end='')
        print(alpha, end='')
        prev = '<'  
    else:
        if alpha == ' ':
            while stack:
                print(stack.pop(), end='')
            print(' ', end='')
        else:
            stack.append(alpha)
        prev = alpha

while stack:
    print(stack.pop(), end='')
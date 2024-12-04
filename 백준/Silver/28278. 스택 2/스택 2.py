import sys
n = int(sys.stdin.readline())


stack = []
for _ in range(n):
    text = sys.stdin.readline().split()
    cmd = int(text[0])
    if cmd == 1:
        num = int(text[1])
        stack.append(num)
    elif cmd == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif cmd == 3:
        print(len(stack))
    elif cmd == 4:
        if stack:
            print(0)
        else:
            print(1)
    elif cmd == 5:
        if stack:
            print(stack[len(stack)-1])
        else:
            print(-1)
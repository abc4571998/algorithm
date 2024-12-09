import sys

n = int(sys.stdin.readline())

answer = 0
for _ in range(n):
    words = list(sys.stdin.readline().strip())
    stack = []
    # 단어 하나씩 돌아가면서 스택 탑과 같은 단어면 뽑아내고, 아니면 스택에 넣기
    for word in words:
        if not stack: # stack 이 비었다면 단어 넣기
            stack.append(word)
        else:
            prev = stack.pop()
            if prev != word:
                stack.append(prev)
                stack.append(word)
  
    if not stack:
        answer += 1

print(answer)
n = int(input())

numbers = [int(input()) for _ in range(n)]

# top 숫자가 나오면
stack = []

num_idx = 0
isPossible = True
result = []
for i in range(1, n+1):
    if i == numbers[num_idx]:
        stack.append(i)
        result.append('+')
        while stack and num_idx < n:
            if stack[-1] != numbers[num_idx]:
                break
            stack.pop()
            result.append('-')
            num_idx += 1
    elif i < numbers[num_idx]:
        stack.append(i)
        result.append('+')
    else:
        isPossible = False
        break
    

if isPossible and not stack:
    print('\n'.join(result))

else:
    print("NO")
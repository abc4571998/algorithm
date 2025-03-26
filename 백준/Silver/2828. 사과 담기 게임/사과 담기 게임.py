n, m = map(int, input().split())
j = int(input())

apple_pos = []
for _ in range(j):
    apple_pos.append(int(input()))

start_pos = 1
end_pos = start_pos + (m-1)

result = 0

for i in range(len(apple_pos)):
    apple = apple_pos[i]
    if start_pos <= apple and end_pos >= apple:
        continue
    elif start_pos > apple:
        result += (start_pos - apple)
        start_pos = apple
        end_pos = apple + m - 1
    elif end_pos < apple:
        result += (apple - end_pos)
        end_pos = apple
        start_pos = apple - m + 1

print(result)
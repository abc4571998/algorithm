num = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
total = 0
for i in data:
  result += i
  total += result

print(total)
num, target = list(map(int, input().split()))
data = []
for i in range(num):
  data.append(int(input()))
data = sorted(data, reverse=True)
count = 0

for i in data:
  if target == 0:
    break
  if target >= i:
    count += (target // i)
    target = target % i

print(count)
num = int(input())
data = []
for _ in range(num):
  data.append(int(input()))

data.sort()
max = data[0] * num
for i in range(1, len(data)):
  tmp_weight = data[i] * (num - i)
  if max < tmp_weight:
    max = tmp_weight

print(max)
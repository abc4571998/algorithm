num = int(input())

sum = 0
count = 0
while True:
  count += 1
  sum += count
  if sum > num:
    break

print(count-1)
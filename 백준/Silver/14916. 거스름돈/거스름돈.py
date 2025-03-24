num = int(input())

cnt = 0
while num > 0:
    if num % 5 == 0:
        cnt += num // 5
        num -= num // 5 * 5
        break
    else:
        num -= 2
        cnt += 1

if (num == 0):
    print(cnt)
else:
    print(-1)
# B 는 고정이고, A 는 정렬해서 B의 최댓값과 A의 최솟값을 곱해준다.
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

sum = 0
for a, b in zip(a, b):
    sum += a * b

print(sum)
n, m = map(int, input().split())

package = []
one = []

for _ in range(m):
    a, b = map(int, input().split())
    package.append(a)
    one.append(b)

min_package = min(package)
min_one = min(one)

result = 0

# 낱개로만 구매하거나
# 패키지 + 낱개로 구매하거나
# 패키지로 다 구매하거나

if min_package > min_one * 6:
    result = min_one * n

else:
    result += (n // 6) * min_package
    n = n % 6
    if min_package > (n * min_one):
        result += n * min_one
    else:
        result += min_package

print(result)
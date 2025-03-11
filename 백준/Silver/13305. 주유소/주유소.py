#거리 반복문을 돌면서 이전 주유소 가격과 곱해서 제일 적은 금액을 선택해 간다.

n = int(input())
loads = list(map(int, input().split()))
prices = list(map(int, input().split()))

result = 0

for i in range(len(loads)):
    load = loads[i]
    min_price = prices[0]
    for j in range(i+1):
        price = prices[j]
        if price < min_price:
            min_price = price
    result += min_price * load

print(result)
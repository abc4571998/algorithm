repeat = int(input())

for j in range(repeat):
    n = int(input())
    prices = list(map(int, input().split()))

    #거꾸로 생각해보기
    max_price = 0
    result = 0
    for i in range(n-1, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]
        else:
            result += max_price - prices[i]

    print(result)
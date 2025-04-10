n, m = map(int, input().split())

# 치킨집과 집간의 거를 계산하는 2차원 배열 만들기
# 치킨집과 집의 좌표를 저장하는 배열도 만들기
# 치킨즙 m 를 꺼내는 경우 계산
# 거낼때의 최소거리를 배열에서 꺼내서 더해보기 

houses = []
stores = []

for i in range(n):
    l = list(map(int, input().split()))
    for j in range(n):
        if l[j] == 1: #집이면
            houses.append((i, j))
        elif l[j] == 2:
            stores.append((i, j))

arr = [[0] * len(houses) for _ in range(len(stores))]

# 치킨거리 계산
for i in range(len(stores)):
    store = stores[i]
    for j in range(len(houses)):
        house = houses[j]
        arr[i][j] = abs(store[0] - house[0]) + abs(store[1] - house[1])

comb_stores = []
def combination(path, start):
    if len(path) == m:
        comb_stores.append(path)
        return

    for i in range(start, len(stores)):
        combination(path + [i], i+1)
    
combination([], 0)

# 한 집에서 치킨거리 구하기

result = 99999
# 치킨집 몇개를 선택 -> 각각 치킨집이 집까지 거리가 얼만지 가져와서 더해줌 -> 그게 최소인거
for chicken in comb_stores:
    total = 0
    for home in range(len(houses)):
        min_dist = 99999
        for c in chicken:
            if min_dist > arr[c][home]:
                min_dist = arr[c][home]
        total += min_dist
    if result > total:
        result = total

print(result)

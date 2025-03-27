n = int(input())
l = list(map(int, input().split()))

# 최소 l[i]번째에는 있어야 하는데 이미 앞에서 차지한 자리라면 (작은애가 차지) 제외하고 다음 자리로
result = [0 for _ in range(n)]

for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == l[i] and result[j] == 0:
            result[j] = i+1
            break
        if result[j] == 0:
            cnt += 1   

print(' '.join(map(str, result)))
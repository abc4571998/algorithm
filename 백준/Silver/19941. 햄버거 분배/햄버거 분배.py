n, k = map(int, input().split())
s = list(input())

#사람이 나오면 자신의 왼쪽중에서 가장 멀리있는 햄버거를 선택한다.

result = 0
for i in range(n):
    if s[i] == 'P': 
        for j in range(max(0, i-k), min(i+k+1, n)):
            if s[j] == 'H': #햄버거면
                s[j] = 0
                result += 1
                break

print(result)
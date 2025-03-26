n = int(input())

scores = [] 

for _ in range(n):
    scores.append(int(input()))

prev = scores[-1]
result = 0

for j in range(len(scores)-1, 0, -1):
    score = scores[j-1]
    if score >= prev:
        diff = score - prev + 1
        result += diff
        prev -= 1
    else:
        prev = score    

print(result)
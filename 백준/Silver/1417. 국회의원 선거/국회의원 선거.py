n = int(input())
dasom = int(input())
votes = []

for _ in range(n-1):
    votes.append(int(input()))

votes.sort(reverse=True)
result = 0

if n == 1:
    print(0)
else: 
    while dasom <= votes[0]:
        votes[0] -= 1
        dasom += 1
        votes.sort(reverse=True)
        result += 1

    print(result)
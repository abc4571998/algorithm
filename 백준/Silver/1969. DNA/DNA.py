from collections import Counter

n, m = map(int, input().split())

dnas = []
alphabets = [[] for _ in range(m)]

for _ in range(n):
    dna = input()
    dnas.append(dna)
    for i in range(m):
        alphabets[i].extend(dna[i])
    
result = ''
cnt = [0 for _ in range(n)]
for i in range(m):
    alphabet = alphabets[i]
    alpha_cnt = Counter(sorted(alphabet))
    most_alpha = alpha_cnt.most_common(1)[0]
    for j in range(n):
        if alphabets[i][j] != most_alpha[0]:
            cnt[j] += 1
    result += most_alpha[0]

print(result)
print(sum(cnt))
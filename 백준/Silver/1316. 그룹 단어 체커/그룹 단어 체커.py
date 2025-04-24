#이전 단어와 같으면 통과. 아니라면 이전에 나오지 않은 단어여야함

n = int(input())
result = 0

for _ in range(n):
    word = list(input())
    word_set = set()
    prev = None
    check = True
    for i in range(len(word)):
        if prev == word[i]:
            continue
        elif word[i] in word_set:
            check = False
            break
        word_set.add(word[i])
        prev = word[i]
    if check:
        result += 1

print(result)

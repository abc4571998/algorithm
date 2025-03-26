from collections import Counter
import sys
#홀수가 한개 이상이면 안됨
s = list(input())
s.sort()

word_counter = Counter(s)

odd_cnt = 0
for value in word_counter.values():
    if value % 2 == 1:
        odd_cnt += 1
    if odd_cnt > 1:
        print("I'm Sorry Hansoo")
        sys.exit()


mid = ''
answer = ''
for key, value in word_counter.items():
    if value % 2 == 1:
        mid = key
        word_counter[key] -= 1
    answer += key* (value//2)

print(answer + mid + answer[::-1])

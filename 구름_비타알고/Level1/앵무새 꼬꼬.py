import re
n = int(input())
answers = []
for i in range(n):
	sentence = input()
	vowels = re.sub('[^aAeEiIoOuU]', '', sentence)
	if len(vowels) == 0: vowels = "???"
	answers.append(vowels)

for answer in answers:
	print(answer)
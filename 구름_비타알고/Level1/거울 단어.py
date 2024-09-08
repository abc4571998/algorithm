mirror_dict = dict({'b': 'd', 'p': 'q', 's': 'z', 'd':'b', 'q':'p', 'z': 's', 'i':'i', 'l':'l', 'm':'m', 'n':'n', 'o': 'o', 'u':'u', 'v':'v', 'w':'w', 'x':'x'})
def check_mirror(front, end):
	for i in range(len(front)):
		if front[i] in mirror_dict and mirror_dict[front[i]] == end[i]: continue
		return False
	return True

n = int(input())

for _ in range(n):
	sentence = input()
	if len(sentence) == 1:
		if sentence in mirror_dict and sentence == mirror_dict[sentence]:
			print('Mirror')
		else: print('Normal')
	else:
		mid = len(sentence) // 2
		front = sentence[:mid]
		end = sentence[mid:]
		end_reverse = end[::-1]

		if check_mirror(front, end_reverse): print('Mirror')
		else: print('Normal')
def convert_original(num, r):
	num = int(num)
	reverse_num = ''
	while num > 0:
		num, mod = divmod(num, r)
		if mod >= 10:
			mod = chr(mod+55)
		reverse_num += str(mod)
	return reverse_num[::-1]

original, converted = input().split()

for r in range(2, 17):
	if converted == convert_original(original, r):
		print(r)
		break
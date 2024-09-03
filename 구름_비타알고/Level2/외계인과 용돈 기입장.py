
n, m = map(int,input().split())
input_list = [0]
input_list.extend(list(map(int, input().split())))
consumption_list = [0]
for i in range(1, n+1):
	consumption_list.append(consumption_list[i-1] + input_list[i])
	
answers = []

for i in range(m):
	start, end = map(int, input().split())
	answers.append(consumption_list[end]-consumption_list[start-1])
	
for answer in answers:
	if answer >= 0:
		print(f"+{answer}")
	else:
		print(answer)
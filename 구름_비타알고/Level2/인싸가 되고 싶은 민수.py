def divisor(num):
	answer = num
	for i in range(2, int(num**(1/2))+1):
		if num % i == 0:
				answer = i
				break
	return answer

start, end = map(int,input().split())
if start != end:
	print(2)

else:
	print(divisor(start))

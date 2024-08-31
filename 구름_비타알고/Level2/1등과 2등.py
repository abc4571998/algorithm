import re

def check_start_12(user_input):
	filter_input = re.sub('12', '-', user_input, count = 1)
	if '-' not in filter_input:
		return False
	filter_input = re.sub('21', '*', filter_input, count = 1)
	if '*' not in filter_input:
		return False
	
	return True
	
def check_start_21(user_input):
	filter_input = re.sub('21', '-', user_input, count = 1)
	if '-' not in filter_input:
		return False
	filter_input = re.sub('12', '*', filter_input, count = 1)
	if '*' not in filter_input:
		return False
	
	return True
		
user_input = input()

if check_start_12(user_input) or check_start_21(user_input): print("Yes")
else: print("No")
	
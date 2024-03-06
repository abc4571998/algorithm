import re

input_str = input()
input_list = re.findall(r'\d+|[-+]', input_str)
sum = 0

is_minus = False
for i in input_list:
  if (i.isdigit()):
    if is_minus == True:
      sum -= int(i)
    else:
      sum += int(i)
  else:
    if i == '-':
      is_minus = True
    elif i == '+' and is_minus == False:
      is_minus = False
  
print(sum)
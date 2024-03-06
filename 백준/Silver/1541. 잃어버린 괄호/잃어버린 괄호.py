input_str = input()
input_str = [sum(map(int, x.split('+'))) for x in input_str.split('-')]  
print(input_str[0] - sum(input_str[1:]))
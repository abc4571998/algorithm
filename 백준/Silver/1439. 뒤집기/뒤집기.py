data = str(input())
data_split_0 = [x for x in data.split('0') if x != '']
data_split_1 =  [x for x in data.split('1') if x != '']
print(str(min(len(data_split_0), len(data_split_1))))
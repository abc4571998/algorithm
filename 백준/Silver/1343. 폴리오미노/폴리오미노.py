words = input().split('.')

result = ''
for word in words:
    if word == '': 
        result += '.'
        continue
    elif len(word) % 2 != 0:
        result = '-1.'
        break
    
    result += (len(word) // 4) * 4 * 'A'
    result += len(word) % 4 * 'B'
    result += '.'

print(result[:-1])
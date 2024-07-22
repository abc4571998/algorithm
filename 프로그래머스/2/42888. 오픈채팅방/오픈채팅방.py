def solution(record):
    info = []
    answer = []
    maps = {}
    for sentence in record:
        parts = sentence.split()
        keyword, username = parts[0], parts[1]
        
        if keyword == 'Enter':
            nickname = parts[2]
            maps[username] = nickname
            info.append([keyword, username])
        elif keyword == 'Change':
            nickname = parts[2]
            maps[username] = nickname
        elif keyword == 'Leave':
            info.append([keyword, username])

    for i in info:
        keyword, username = i[0], i[1]
        if keyword == 'Enter':
            answer.append(maps[username]+'님이 들어왔습니다.')
        else:
            answer.append(maps[username]+'님이 나갔습니다.')
    return answer
a = ['A', 'E', 'I', 'O', 'U']
idx = -1
answer = 0

def solution(word):
    #for i in range(len(word)):
    #    alphabet = word[i]
    #    index = a.index(alphabet)
    #    print('alphabet ', alphabet, index)
    #    answer += (5**(5-i)-1) / (5 - 1) * (index) + 1
    def dfs(cnt, s):
        global idx, answer
        if cnt <= 5:
            idx += 1
            if s == word:
                answer = idx
                return 
        else:
            return
        for i in range(5):
            dfs(cnt+1, s+a[i])
    dfs(0, '')
    return answer
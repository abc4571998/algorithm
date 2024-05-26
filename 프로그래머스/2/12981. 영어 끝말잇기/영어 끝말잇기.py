import math

def solution(n, words):
    answer = []
    previous_word = words[0][0]
    for index, word in enumerate(words):
        start_word = word[0]
        target = (index+1)%n
        time = math.ceil((index+1)/n)
        if target == 0: target = n
		# 다른 단어를 이야기 하면 탈락
        if previous_word != start_word:
            return [target, time]
        # 이미 말한 단어가 있으면 탈락
        elif words[0:index].count(word) >= 1:
            return [target, time]
        # 한 글자는 탈락
        elif len(word) == 1:
            return [target, time];
        previous_word = word[-1]
    return [0,0]
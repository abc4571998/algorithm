from collections import deque

def is_one_letter_diff(word1, word2):
    diff_count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            diff_count += 1
        if diff_count > 1:
            return False
    return diff_count == 1

def find_one_diff_letter(target, words, begin):
    result = []
    queue = deque([(target, words, 0)])
    while queue:
        target_word, words_list, count = queue.popleft()
        print("**", target_word, words_list, count)
        for word in words_list:
            if is_one_letter_diff(target_word, begin):
                print(target_word, begin)
                return count+1
            if is_one_letter_diff(target_word, word):
                queue.append((word, [x for x in words if x != target_word], count+1))
    return 0

def solution(begin, target, words):
    answer = 0
    #1. target 에서 한글자 바꾼 단어들을 큐에 넣는다.
    if target not in words:
        return answer
    answer = find_one_diff_letter(target, words,begin)
    return answer
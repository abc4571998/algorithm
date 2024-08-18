from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_dict = defaultdict(list)
    
    #1. 고유번호 처리를 기존 튜플에 추가하기 (고유번호, i)
    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_dict[genre].append((play, i))
    
    sorted_genre = sorted(genre_dict.items(), key=lambda x: sum(play for play, _ in x[1]), reverse=True)
    
    for genre, play_list in sorted_genre:
        play_list = sorted(play_list, key=lambda x: (-x[0], x[1])) 
           
        # 2. 마지막에 재생횟수 배열에서 최대 두개를 선택하기
        for i in range(min(2, len(play_list))):
            answer.append(play_list[i][1])
    return answer
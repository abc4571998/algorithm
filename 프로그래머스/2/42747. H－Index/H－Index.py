def solution(citations):
    answer = 0
    # 정렬
    citations.sort(reverse=True)
    # for 문 돌면서 누적 논문 i편보다 citation 을 비교
    for i in range(len(citations)):
        citation = citations[i]
        if citation >= i+1:
            answer = i+1
        else:
            break
    return answer
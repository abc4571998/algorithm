import math

def get_divisor(num):
    divisor = []
    sqrt_num = int(math.sqrt(num))
    for i in range(1, sqrt_num + 1 ):
        if num % i == 0:
            divisor.append(i)
            if i != num // i:
                divisor.append(num // i)
    divisor.sort()
    return divisor

def solution(brown, yellow):
    answer = []
    # 브라운과 엘로우의 합은 가로 x 세로
    sum = brown + yellow
    # yellow 약수로 찾아보기
    sum_divisor = get_divisor(yellow)
    # 가로 >= 세로, yellow 약수 중간부터 끝까지 돌면서 중앙에 위치하는 경우의 수 보기
    for i in range(len(sum_divisor)//2,len(sum_divisor)):
        # yellow 가로와 세로
        width = sum_divisor[i]
        height = int(yellow/width)
        # brown 는 yellow 를 감싸고 있음
        brown_count = (width+2)*2 + (height*2)
        # 감싸는 brown 개수랑 실제 brown 개수랑 같다면 리턴
        if brown_count == brown:
            return [width+2, height+2]
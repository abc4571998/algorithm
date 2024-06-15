def solution(arr1, arr2):
	# arr1 요소뽑고 arr2 요소를 뽑아서 arr1 의 행과 arr2 의 열 곱하기
    arr = [[sum([element1[i] * arr2[i][j] for i in range(len(arr2))]) for j in range(len(arr2[0]))] for element1 in arr1]
    #[[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
    return arr
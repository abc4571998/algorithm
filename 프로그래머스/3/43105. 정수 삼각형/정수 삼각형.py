def solution(triangle):
    dp = [0] * ((500*501)//2 + 1)
    dp[1] = triangle[0][0]
    for i in range(len(triangle)-1):
        #현재 높이의 원소
        element_arr = triangle[i]
        for j in range(len(element_arr)):
            left_child = triangle[i+1][j]
            right_child = triangle[i+1][j+1]
            current_idx = (i*(i+1))//2 + 1 + j
            left_child_idx = ((i+1)*(i+2))//2 + 1 + j
            right_child_idx = ((i+1)*(i+2))//2 + 1 + j+1
            dp[left_child_idx] = max(dp[left_child_idx], dp[current_idx]+left_child)
            dp[right_child_idx] = max(dp[right_child_idx], dp[current_idx]+right_child)
    return max(dp)
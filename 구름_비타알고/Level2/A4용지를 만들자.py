n, m = map(int, input().split())

# 1. A4 가로로 했을때 가로40*세로20
case1 = (n//40) * (m//20)
# 2. A4 세로로 했을때 가로20*세로40
case2 = (n//20) * (m//40)
# 3. 정사각형 모양 가로40*세로40
case3 = (n//40) * (m//40)
print(case1+case2-(case3*2))

n = int(input())

#((i//9)%3 == 1 and (j//9)%3 == 1) or ((i//3)%3 == 1 and (j//3)%3 == 1) or ((i//1)%3 == 1 and (j//1)%3 == 1) 규칙일때 빈칸
def check_range(i, j):
    num = n // 3
    while num != 0:
        #print(num,i,j, (i//num)%3, (j//num)%3)
        if (i//num)%3 == 1 and (j//num)%3 == 1: return True
        num = num // 3

    return False

for i in range(n):
    for j in range(n):
        #print(j)
        num = n // 3
        if check_range(i, j): print(" ", end='')
        else: print("*", end='')
    print()
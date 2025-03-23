num = input()

if '0' not in num:
    print(-1)

else:
    # 1. 3의 배수인지 확인
    sum_num = sum(map(int, num))
    if sum_num % 3 != 0:
        print(-1)

    else:
        # 2. 내림차순 정렬
        num = sorted(num, reverse=True)
        print(''.join(num))
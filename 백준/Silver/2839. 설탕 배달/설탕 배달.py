def calc_sugar(n):
    for i in range((n//5), -1, -1):
        if (n - 5 * i) % 3 == 0:
            return i + (n - 5 * i) // 3
    return -1

num = int(input())

print(calc_sugar(num))
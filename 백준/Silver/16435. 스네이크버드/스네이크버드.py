n, snake_len = map(int, input().split())

fruits = list(map(int, input().split()))
fruits.sort()

for fruit in fruits:
    if fruit <= snake_len:
        snake_len += 1

print(snake_len)

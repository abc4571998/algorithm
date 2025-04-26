def dfs(arr, current: list, i):
    if len(current) == 6:
        print(" ".join(map(str, current)))
        return
    # 붙여서 보내거나 그냥 보내거나
    if i >= len(arr):
        return
    dfs(arr, current + [arr[i]], i+1)
    dfs(arr, current, i+1)

while True:
    arr = list(map(int, input().split()))
    if len(arr) == 1 and arr[0] == 0:
        break
    arr = arr[1:]
    dfs(arr, [], 0)
    print()
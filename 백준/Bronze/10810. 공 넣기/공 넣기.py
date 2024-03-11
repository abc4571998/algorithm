n, m = map(int, input().split())
bucket = [0 for x in range(n)]
for i in range(m):
    start, end, num = map(int, input().split())
    bucket[start-1:end] = [num for x in range(end-start+1)]
print(' '.join(str(x) for x in bucket))
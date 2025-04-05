import sys
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    l = []
    for i in range(n):
        l.append(tuple(map(int, sys.stdin.readline().split())))
    l.sort()
    cnt = 1
    best = l[0][1]
    for j in range(1,  len(l)):
        if best > l[j][1]:
           cnt += 1
           best = l[j][1]
    print(cnt)
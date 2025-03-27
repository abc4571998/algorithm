n, l = map(int, input().split())
hole_pos = list(map(int, input().split()))

hole_pos.sort()

# 테이프로 이미 커버가 된 구멍인지 확인 필요
current_tape = 0
result = 0

for i in range(len(hole_pos)):
    hole = hole_pos[i]
    if hole > current_tape:
        result += 1
        current_tape = hole + (l-1)

print(result)

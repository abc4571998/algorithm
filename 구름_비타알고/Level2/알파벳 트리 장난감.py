alphabet_dict = {chr(i): i - 64 for i in range(65, 91)}

def find_min_value(tree, parent, value):
    left = 2 * parent + 1
    right = left + 1
    value += alphabet_dict[tree[parent]]

    # 종료 조건: 리프 노드에 도달했을 때
    if left >= len(tree):
        return value

    # 자식 노드 중 작은 값을 가지는 노드를 따라감
    left_value = find_min_value(tree, left, value)
    right_value = find_min_value(tree, right, value)
    return min(left_value, right_value)

def find_max_value(tree, parent, value):
    left = 2 * parent + 1
    right = left + 1
    value += alphabet_dict[tree[parent]]

    # 종료 조건: 리프 노드에 도달했을 때
    if left >= len(tree):
        return value

    # 자식 노드 중 큰 값을 가지는 노드를 따라감
    left_value = find_max_value(tree, left, value)
    right_value = find_max_value(tree, right, value)
    return max(left_value, right_value)

n = int(input())
tree = []
for _ in range(n):
    tree.extend(list(input().strip()))

print(find_min_value(tree, 0, 0))
print(find_max_value(tree, 0, 0))

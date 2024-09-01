def calc_exp(left, right, oper): #eval 함수 사용이 안되므로 직접 구현
    if oper == '+':
        return left+right
    elif oper == '-':
        return left-right
    elif oper == '*':
        return left*right
    elif oper == '/':
        return left//right
    
def eval_tree(nodes, answer, current):
    if current[1] != None: #자식이 있는 연산자 노드는 왼쪽 자식과 오른쪽 자식을 연산해야 함
        left_value = eval_tree(nodes, answer, nodes[current[1]-1])
        right_value = eval_tree(nodes, answer, nodes[current[2]-1])
        return calc_exp(left_value, right_value, current[0])
    else: #자식 노드가 없다면 (리프노드라면) 값만 리턴
        return current[0]

for k in range(10):
    n = int(input())
    nodes = [[None]*3 for _ in range(n)] 
    # nodes 안에 [현재 노드의 값, 왼쪽 자식 노드, 오른쪽 자식 노드] 로 저장하려고 함
    for i in range(n):
        s = input().split()
        if s[1].isdigit(): # 현재 노드가 숫자면 자식은 없으므로 [현재 노드값, None, None] 으로 저장
            nodes[i][0] = int(s[1])
        else: # 현재 노드가 연산자면 자식 노드도 함께 적어줌
            left, right = int(s[2]), int(s[3])
            nodes[i] = [s[1], left, right]
        
    print(f"#{k+1} {eval_tree(nodes, 0, nodes[0])}")
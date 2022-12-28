a = list(map(int, input().split()))

tree = None

for i in a: # 将列表元素插入排序二叉树中
    if tree == None:
        tree = [i, None, None]
    else:
        u = tree
        while u != None:
            fa = u
            if i <= u[0]:
                op = 1
            else:
                op = 2
            u = fa[op]
        fa[op] = [i, None, None]

st = [[tree, 0]]
while len(st):
    u, op = st.pop()
    if op == 1:
        print(u)
    else:
        if u[2] != None:
            st.append([u[2], 0])
        st.append([u[0], 1])
        if u[1] != None:
            st.append([u[1], 0])
    

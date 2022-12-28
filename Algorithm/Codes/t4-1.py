pre_order = input()  # 输入前序遍历
pointer = 0
L = 32 # 图片的长宽
pixel = [[0] * L for i in range(L)]  # pixel记录每个像素的颜色，0表示白，1表示黑
stack = [[0, 0, L]]
cnt = 0

while len(stack):
    r, c, w = stack[-1] # 绘制以(r,c)为左上角，长宽为w的图像
    stack.pop()
    ch = pre_order[pointer]
    pointer += 1
    if ch == 'p':
        stack.append([r + w // 2, c + w // 2, w // 2])
        stack.append([r + w // 2, c, w // 2])
        stack.append([r, c, w // 2])
        stack.append([r, c + w // 2, w // 2])
    elif ch == 'f':
        for i in range(r, r + w):
            for j in range(c, c + w):
                if pixel[i][j] == 0:
                    pixel[i][j] = 1
                    cnt += 1
print(cnt)
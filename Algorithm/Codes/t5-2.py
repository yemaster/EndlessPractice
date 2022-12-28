n = int(input())
h = [0]
for i in range(n):
    h.append(int(input()))
iCow = [0] * (n + 1)
st = []
for i in range(n, 0, -1):
    while len(st) > 0 and h[i] >= h[st[-1]]:
        st.pop()
    if len(st) == 0:
        iCow[i] = 0
    else:
        iCow[i] = st[-1]
    st.append(i)
for i in range(1, n + 1):
    print(iCow[i])

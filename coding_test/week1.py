from sys import stdin

n, k = map(int, stdin.readline().split())
st = []
good = 0

for i in range(n):
    name = input().strip()
    st.append((i, len(name), name))

st.sort(key=lambda x: x[1])

for i in range(n-1):
    idx = i+1
    while idx < n and st[idx][1] == st[i][1]:
        if st[idx][0] - st[i][0] <= k:
            good += 1
        idx += 1
print(good)
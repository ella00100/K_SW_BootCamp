from sys import stdin

n, m = map(int, stdin.readline().split())
cn, cm, d = map(int, stdin.readline().split())
dmap = []

#d = 0,1,2,3 = 북(위), 동(오), 남(아), 서(왼)

for i in range(n):
    h = list(map(int, stdin.readline().split()))
    dmap.append(h)

count = 0

while True:
    if dmap[cn][cm] == 0:
        dmap[cn][cm] = 1
        count += 1

    print(dmap)
    if ( cn ==0 or  dmap[cn - 1][cm] == 1) and ( cm == 0 or dmap[cn][cm - 1] == 1) and \
            ( cn == n-1 or dmap[cn + 1][cm] == 1) and ( cm== m-1 or dmap[cn][cm + 1] == 1):
        if d == 0:
            if cm < m-1:
                cm = cm + 1
            else:
                break
        elif d == 1:
            if cn > 0:
                cn = cn - 1
            else:
                break
        elif d == 2:
            if cm > 0:
                cm = cm - 1
            else:
                break
        elif d == 3:
            if cn < n-1:
                cn = cn + 1
            else:
                break
    else:
        if cn == 0 and d == 0 and cm == 0:
            cn += 1
            cm += 1

        if d == 0:
            d = 3
            if cn > 0 and dmap[cn-1][cm] == 0:
                cn = cn - 1
        elif d == 1:
            d = 0
            if cm > 0 and dmap[cn][cm-1] == 0:
                cm = cm - 1
        elif d == 2:
            d = 1
            if cn < n-1 and dmap[cn+1][cm] == 0:
                cn = cn + 1
        elif d == 3:
            d = 2
            if cm < m-1 and dmap[cn][cm+1] == 0:
                cm = cm + 1

print(count)

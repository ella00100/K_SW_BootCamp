def fibo_recu(n) :
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        return fibo_recu(n - 1) + fibo_recu(n - 2)

#속도 개선
def fibo_iter(n):
    r = list()
    p1, p2 = 1, 1
    for _ in range(n):
        r.append(p1)
        p1, p2 = p2, p1 + p2
    return r[-1]

print("## 피보나치 수 ##")

for i in range(2, 20) :
    print(fibo_recu(i), end=' ')

print()

for i in range(2,20):
    print(fibo_iter(i), end = ' ')

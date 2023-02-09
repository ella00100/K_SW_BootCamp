g_memo = [None for _ in range(50)]
g_memo[0], g_memo[1] = 0,1

def fibo_memo_recu(n):
    """
    재귀함수에 Memoization(DP)을 사용한 피보나치 수열 처리 함수
    :param n:
    :return:
    """
    global g_memo, count_memo_recu
    count_memo_recu = count_memo_recu + 1

    if n <= 1:
        return g_memo[n]

    if g_memo[n] is not None:  # 전역 메모리 memos에 이전에 계산한 결과 값이 존재하면
        return g_memo[n]

    g_memo[n] = fibo_memo_recu(n - 2) + fibo_memo_recu(n - 1)  # 처음 방문하는 n이면
    return g_memo[n]

def fibo_memo(n):
    """
    Memoization(DP)을 사용한 피보나치 수열 처리 함수
    :param n:
    :return:
    """
    global count_memorization
    count_memorization = count_memorization + 1
    memo = [0, 1]
    if n <= 1:
        return memo[n]
    else:
        for i in range(2, n+1):
            memo.append(memo[i-1] + memo[i-2])
        return memo[n]

def fibo_recu(n):
    """
    재귀를 이용한 피보나치 수열 함수
    :param n:
    :return:
    """
    global count_recursion
    count_recursion += 1
    if n == 0:
        return 0
    elif n == 1 :
        return 1
    else:
        return fibo_recu(n-1) + fibo_recu(n-2)

#속도 개선
def fibo_iter(n):
    """
    반복문을 이용한 피보나치 수열 함수
    :param n:
    :return:
    """
    r = list()
    p1, p2 = 1, 1
    for _ in range(n):
        r.append(p1)
        p1, p2 = p2, p1 + p2
    return r[-1]

count_recursion = 0
count_memorization = 0
count_memo_recu = 0

print("## 피보나치 수 ##")

for i in range(2,20):
    print(fibo_memo(i), end = ' ')
print()
for i in range(2, 20) :
    print(fibo_recu(i), end=' ')
print()
for i in range(2,20):
    print(fibo_memo_recu(i), end = ' ')
print()
print(f'메모 : {count_memorization}, 재귀 : {count_recursion}, 재귀메모 : {count_memo_recu}')

for i in range(2,20):
    print(fibo_iter(i), end = ' ')

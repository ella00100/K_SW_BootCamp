def factorial_iter(n):
    """
    반복문을 이용한 팩터리얼 함수
    :param n: n!
    :return:  integer 팩토리얼 계산 결과 값
    """
    result = 1
    for k in range(1,n+1):
        result = result * k
    return  result

def fatorial_recu(n):
    """
    재귀 함수를 이용한 팩토리얼 함수
    :param n: n!
    :return:  자기 자신을 호출 또는 1
    """
    if n == 1:
        return 1
    else:
        return fatorial_recu(n-1)*n


print(factorial_iter(5))
print(fatorial_recu(5))
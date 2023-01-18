#Lambda

#기본 함수 사용
import random

def process(no_list, f):
    for n in no_list:
        print(f(n))

def squares(n):
    """
    제곱 함수
    :param n: 정수(integer)
    :return:  제곱 수 (squares)
    """
    return n*n

numbers = [random.randint(1,100) for i in range(5)]
print(numbers)
process(numbers,squares)

#Lambda 사용
def process_l(no_list,f):
    for n in no_list:
        print(f(n))

numbers = [random.randint(1,100) for i in range(5)]
print(numbers)
process(numbers, lambda x: x*x)

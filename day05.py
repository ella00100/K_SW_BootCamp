#function

def sixty():
    """
    숫자 60을 출력하는 함수
    """
    print(60)

def call_func(f):
    """
    매개변수로 함수를 넘겨받아 실행
    :param f: 매개변수는 function(함수)
    :return:
    """
    f()

call_func(sixty)

def substract(n1,n2):
    """
    n1-n2 빼기 연산을 실행하는 함수
    """
    print(n1-n2)

def run_fun(f, arg1, arg2):
    """
    함수를 매개변수로 받아 함수 안에서 함수를 실행
    :param f: 실행할 함수
    :param arg1: 매개변수 1
    :param arg2: 매개변수 2
    :return:
    """
    f(arg1,arg2)

run_fun(substract,10,5)

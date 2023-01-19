#decorator

def sub_int(x,y):
    return x - y

def document_it(func): #decorator 생성
    def new_function(*args, **kwargs):
        print('실행 중인 함수: ', func.__name__)
        print('위치 기반 인수들: ', args)
        print('키워드 기반 인수들:', kwargs)
        result = func(*args, **kwargs)
        print('실행 결과: ', result)
        return result
    return new_function

print(sub_int(7,3))
info_sub_int = document_it(sub_int)
info_sub_int(7,3)
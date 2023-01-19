#namespace
g = 1   #전역변수

def print_global():
    print(g)    # g가 전역변수로 이미 선언되어 있으므로
                # 함수 내에서 정의하지 않아도 사용 가능

print_global()  # 전역변수 g를 print 하는 함수 => 1 출력
print(g)        # 전역변수 g를 print => 1 출력

def print_local():
    g=2         # 지역변수 g값을 2로 할당
    print(g)

print_local()   # 지역변수 g를 출력하는 함수 => 2 출력
print(g)        # 전역변수 g는 변하지 않았음 = > 1 출력

def change_print_global():
    global g    # 전역변수 g를 불러옴
    g=3         # 전역변수 g 값을 3으로 변경
    print(g)

change_print_global() # 3 출력
print(g)              # 전역변수 자체가 바뀌었으므로 3출력


#generator

def a():      #generator
    yield 1
    yield 2   #값을 저장하지 않으므로 2로 변화
    yield 3

def b():      #nomal function
    return 1  #stop here
    return 2
    return 3

c = a()      #generator 객체 생성
for x in c:
    print(x) #a를 돌면서 1,2,3 차례대로 출력

for x in c:
    print(x) #generator는 한번 순회하면 값이 사라지므로 아무런 출력 x

print(b())   # 1만 출력하고 정지
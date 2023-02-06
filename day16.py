stack = [None for _ in range (5)]  #빈 공간 5자리 생성
top = -1 #초기 상태

top += 1            #top을 증가시켜 준 뒤
stack[top] = "커피"  # 그 자리에 데이터 삽입
top += 1
stack[top] = "녹차"
top += 1
stack[top] = "꿀물"
top += 1
stack[top] = "카푸치노"
top += 1
stack[top] = "바닐라 라떼"

print("_______스택 데이터 생성________")
for i in range(len(stack)-1,-1,-1):
    print(stack[i])

data = stack[top]
stack[top] = None
top -= 1

print("_______스택 데이터 추출 pop________")
for i in range(len(stack)-1,-1,-1):
    print(stack[i])

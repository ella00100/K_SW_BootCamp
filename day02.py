PI = 3.14
print(f'원주율의 값은 {PI}이고 타입의 {type(PI)}입니다')

math_values = (3.24, 2.71) #튜플 생성
print(f'원주율의 값은 {math_values}이고 타입은 {type(math_values)}입니다)')
math_values[0] = 9.99 #튜플은 값을 변경할 수 없음
print(f'원주율의 값은 {math_values}이고 타입은 {type(math_values)}입니다)')
#에러 발생

math_values = [3.24, 2.71] #리스트 생성
print(f'원주율의 값은 {math_values}이고 타입은 {type(math_values)}입니다)')
math_values[0] = 9.99 #리스트는 값을 변경할 수 있음
print(f'원주율의 값은 {math_values}이고 타입은 {type(math_values)}입니다)')
#9.99 2.71 출력
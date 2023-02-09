def Decimical_to_what(base,num):
    if num < base:                  # 숫자가 입력한 진수 보다 작으면
        print(number_array[num], end = '')   # number_array의 해당 값 출력  (ex, 8진수, 3이면 3출력)
    else:                           # 진수 보다 크다면
        Decimical_to_what(base,num//base) # 입력된 숫자를 진수로 나눠 재귀함수 호출
        print(number_array[num%base], end = '')              # 숫자를 진수로 나눈 나머지 출력

number_array = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

inum = int(input('10진수 입력 ---> '))
print('2진수 :', end = ' ')
Decimical_to_what(2,inum)
print('\n8진수 :', end = ' ')
Decimical_to_what(8,inum)
print('\n10진수 :', end = ' ')
Decimical_to_what(10,inum)
print('\n16진수 :', end = ' ')
Decimical_to_what(16,inum)

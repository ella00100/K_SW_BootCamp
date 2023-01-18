#function : prime number

#함수 정의
def isprime(n):
    """
    매개변수로 받은 정수(n)가 소수인가를 판정하는 함수
    :param n : integer number
    :return  : true of false
    """
    if n <= 1:
        return False
    for k in range(2,n):
        if n % k == 0:
            return False
    else:
        return True

#isprime 작동 확인
print(isprime(7))  #True
print(isprime(10)) #False
help(isprime) #함수 내부의 주석처리한 부분 출력

#프로그램 시작
start = int(input("input start number : "))
end = int(input("input end number : "))

if end < start :
    start, end = end, start
for i in range(start, end+1):
    if isprime(i):
        print(i, end = ' ')
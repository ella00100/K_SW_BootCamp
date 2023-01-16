#prime number _ for2

number = int(input("input number : "))
counts = 0

for k in range(2,number):
    if number % k == 0:
        counts = counts + 1
if counts: #0이면 False 0이 아니면 True
    print(f'{number} is NOT prime number!')
else:
    print(f'{number} is prime number!')

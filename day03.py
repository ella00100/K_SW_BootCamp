#구구단_for

while True:
    dan = int(input('Dan : '))

    if dan == 0:
        break
    if 1 < dan <10:
        i = 1
        for i in range(1,10):
            print('{0} * {1} = {2}'.format(dan,i,dan*i))
    else:
        print('2에서 9사이의 값을 입력 하세요')


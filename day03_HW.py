#prob 6.2

guess_me = 7
number = 1

while True:
    if guess_me > number:
        print('too low')
    elif guess_me == number:
        print('found it!')
        break
    else:
        print('oops')
        break
    number += 1
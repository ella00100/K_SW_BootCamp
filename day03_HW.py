#prob 6.3

guess_me = 5

for i in range(10):
    if guess_me > i:
        print('too low')
    elif guess_me == i:
        print('found it!')
        break
    else:
        print('oops')
        break
    i += 1
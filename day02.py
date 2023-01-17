#Chap 4

import random

limits = 20
tweets = "pass" * random.randint(1,10)
diff = limits - len(tweets)
if diff >=0:
    print(tweets)
else:
    print(f"제한 글자 수 {abs(diff)}초과")


vowels = 'aeiou'
letter = 'u'
if letter in vowels:
    print(f'{letter} in vowels')
else:
    print(f'{letter} not in vowels')


a=[]
print(bool(a))
a.append(5)
print(bool(a))
print(bool(set(a)))
print(bool(dict()))
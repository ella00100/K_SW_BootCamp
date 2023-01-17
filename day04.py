import random

#결합하기
first = {'a' : 'agony', 'b' : 'bliss'}
second = {'b' : 'bagles', 'c' : 'candy'}
third = {**first, **second} #first와 second 결합  **
print(third)

#update
fourth = {'c' : 'card', 'd' : 'date'}
third.update(fourth)
print(third)

#in
print('c' in third) #key가 있으면 TRUE 반환
print('card' in third) #card는 value이므로 False 반환

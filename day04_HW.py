#prob 8.6
life = {'animals' : {'cats': 'Henri', 'octopi': 'Grumpy', 'emus': 'Lucy'},
        'plants': {},
        'other' : {}
        }

#prob 8.7
for k in life:
    print(k, end= ' ')
print("\n")

#prob 8.8
for k in life['animals']:
    print(k, end= ' ')
print("\n")

#prob 8.9
print(life['animals']['cats'])
#prob 8.1
e2f = dict(dog='chien',
           cat = 'chat',
           walrus = 'morse')

#prob 8.2
print(e2f["walrus"])

#prob 8.3
f2e = {}
for k, v in e2f.items():
    f2e.update({v:k})
print(f2e)

#prob 8.4
for k, v in e2f.items():
    if v =='chien':
        print(k)

#prob 8.5
for k in e2f:
    print(k, end = ' ')
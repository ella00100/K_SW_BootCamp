#prob 7.11
start1 = ['fee', 'fie','foe']
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the call"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
    ]
start2 = "Someone better"

for k in range(len(rhymes)):
    for i in range(len(start1)):
        start1[i] = start1[i].title()
        print(f'{start1[i]}!', end = ' ')
    print(f'{rhymes[k][0].title()}!')
    print(f'{start2} {rhymes[k][1]}.')
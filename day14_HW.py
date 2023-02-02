#prob 10.5

el_dict = dict( name = 'Hydrogen',
                symbol = 'H',
                number = 1
                )

class Element():
    def __init__(self, dic):
        self.name = dic['name']
        self.symbol = dic['symbol']
        self.number = dic['number']

hydragon = Element(el_dict)
print(hydragon.number)
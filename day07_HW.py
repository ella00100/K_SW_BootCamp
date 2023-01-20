#prob 10.6

class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        import pprint
        pprint.pprint(vars(self))

hydragon = Element('Hydragen','H',1)
hydragon.dump()

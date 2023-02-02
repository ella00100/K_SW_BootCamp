#prob 10.7

class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(vars(self))

hydrogen = Element('Hydrogen','H',1)
hydrogen.dump()

class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return f'{vars(self)}'

hydrogen = Element('Hydrogen','H',1)

print(hydrogen)
print(dir(Element))
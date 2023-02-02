#prob 10.4

class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

ex = Element('Hydrogen', 'H', 1)
print(ex.name, ex.symbol, ex.number)
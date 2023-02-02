# prob 10.8

class Element:
    def __init__(self,name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    def dump(self):
        print(vars(self))

    @property
    def get_name(self):
        return self.__name

    @property
    def get_symbol(self):
        return self.__symbol

    @property
    def get_number(self):
        return  self.__number

    @get_name.setter
    def name_setter(self,name):
        self.__name = name

    @get_symbol.setter
    def symbol_setter(self,symbol):
        self.__symbol = symbol

    @get_number.setter
    def number_setter(self,number):
        self.__number = number

hydrogen = Element('Hydrogen','H',1)
print(hydrogen.get_name)

hydrogen.name_setter = 'Hydrrrgen'
print(hydrogen.get_name)
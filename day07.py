#getter/setter 매서드

class Duck():
    def __init__(self,input_name):
        self.hidden_name = input_name

    def get_name(self):
        print('inside the getter')
        return self.hidden_name

    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

    name = property(get_name, set_name)

don = Duck('Donald')
print(don.get_name())

don.name='Donna'
print(don.name)

don.set_name('InDuck')
print(don.name)

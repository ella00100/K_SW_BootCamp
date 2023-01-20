#다중상속

class Animal:   #할아버지
    def says(self):
        return "I speak!"

class Horse(Animal):
    def says(self):
        return 'Neigh!'

class Donkey(Animal):
    def says(self):
        return 'Hee-Haw!'
    pass

class Mule(Donkey, Horse):   #Donkey가 우선순위
    pass

class Hinny(Horse, Donkey): #Horse가 우선순위
    pass

mule = Mule()
hinny = Hinny()

print(mule.says())
print(hinny.says())
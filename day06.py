#class

# class Pokemon:
#     def __init__(self): #객체 생성 시 동작
#         print("포켓몬 객체 생성됨")
#
# p1 = Pokemon()
# p2 = Pokemon()
# print(p1,p2)

class Pokemon:
    def __init__(self,name,owner,skills):
        self.name = name
        self.owner = owner
        self.skills = skills.split('/')
        print(f'{name} 생성됨')

    def info(self):  #멤버 함수
        print(f'{self.owner}의 포켓몬은 {self.name}입니다')
        for skill in self.skills:
            print(skill)

p1 = Pokemon("피카츄",'한지우','50만 볼트/100만 볼트')
p2 = Pokemon("꼬부기",'오바람','고속스핀/거품물기/몸통박치기/하이드로펌프')

p1.info()
print(p2.skills)

#상속
class Pikachu(Pokemon):
    pass

pi1 = Pikachu("피카츄","덴트","번개")
pi1.info() #다른 정의 없이 부모의 매서드를 사용가능
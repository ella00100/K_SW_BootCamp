#inherit

class Pokemon:
    def __init__(self,owner,skills):
        self.owner = owner
        self.skills = skills.split('/')
        print(f'포켓몬 생성 :', end = ' ' )

    def info(self):
        print(f'{self.owner}의 포켓몬이 사용 가능한 스킬 : {self.skills}')

    def attack(self,idx):
        print(f'{self.skills[idx]} 공격 개시!')
#상속
class Pikachu(Pokemon):
    def __init__(self,owner,skills):
        super().__init__(owner, skills)  #부모 클래스 호출 "포켓몬 생성 : "출력
        self.name = "꼬부기"
        print(f'{self.name}')

    def attack(self, idx):    #부모의 매서드 attck 오버 라이트  => 자식 Pikachu만 가짐
        print(f'나와라 {self.name}! {self.skills[idx]} 공격 개시!')

class Ggoboogi(Pokemon):
    def __init__(self,owner,skills):
        super().__init__(owner,skills)
        self.name = "꼬부기"
        print(f'{self.name}')

    def attack(self, idx):
        print(f'나와라 {self.name}! {self.skills[idx]} 공격 개시!')

    def swim(self):    #꼬부기만 가지는 매서드
        print("음↓ 파↑ 음↓ 파↑")

pi1 = Pikachu("한지우","100만 볼트/번개")
pi1.info() #부모 클래스의 매서드 사용

goo1 = Ggoboogi("오바람","고속 스핀/몸통 박치기")
goo1.attack(1)
goo1.swim()
# inherit

class Pokemon:
    def __init__(self, owner, skills):
        self.owner = owner
        self.skills = skills.split('/')
        print(f'포켓몬 생성 :', end=' ')

    def info(self):
        print(f'{self.owner}의 포켓몬이 사용 가능한 스킬')
        for i in range(len(self.skills)):
            print(f'{i+1} : {self.skills[i]}')

    def attack(self, idx):
        print(f'{self.skills[idx]} 공격 개시!')


# 상속
class Pikachu(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)  # 부모 클래스 호출 "포켓몬 생성 : "출력
        self.name = "꼬부기"
        print(f'{self.name}')

    def attack(self, idx):  # 부모의 매서드 attck 오버 라이트  => 자식 Pikachu만 가짐
        print(f'나와라 {self.name}! {self.skills[idx]} 공격 개시!')


class Ggoboogi(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "꼬부기"
        print(f'{self.name}')

    def attack(self, idx):
        print(f'나와라 {self.name}! {self.skills[idx]} 공격 개시!')

    def swim(self):  # 꼬부기만 가지는 매서드
        print("음↓ 파↑ 음↓ 파↑")


class Pairi(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)  # 부모 클래스 호출 "포켓몬 생성 : "출력
        self.name = "파이리"
        print(f'{self.name}')

    def attack(self, idx):  # 부모의 매서드 attck 오버 라이트  => 자식 Pikachu만 가짐
        print(f'나와라 {self.name}! {self.skills[idx]} 공격 개시!')


while True:
    menu = input('1) 포켓몬 생성 2) 프로그램 종료 : ')
    if menu == '2':
        print('프로그램을 종료합니다')
        break
    elif menu == '1':
        pokemon = input('1) 피카츄 2) 꼬부기 3) 파이리 : ')
        if pokemon == '1':
            name = input('플레이어 이름 입력 : ')
            skill = input('사용 가능한 기술 입력 (/로 구분) : ')
            p = Pikachu(name, skill)
        elif pokemon == '2':
            name = input('플레이어 이름 입력 : ')
            skill = input('사용 가능한 기술 입력 (/로 구분) : ')
            p = Ggoboogi(name, skill)
        elif pokemon == '3':
            name = input('플레이어 이름 입력 : ')
            skill = input('사용 가능한 기술 입력 (/로 구분) : ')
            p = Pairi(name, skill)
        else:
            print('주어진 선택지에서 골라주세요')

        p.info()
        attack_menu = input('공격 번호 선택 : ')
        p.attack(int(attack_menu)-1)

    else:
        print('주어진 선택지에서 골라주세요')
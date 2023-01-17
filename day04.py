import random

alcohol_foods = dict(beer = 'chicken',soju = 'tomato', wine ='cheese',makguli = 'fish & Chips')
alcohol_list = list(alcohol_foods)

food_list = [food for food in alcohol_foods.values()]
while True:
    alcohol = int(input(f"술을 선택 하세요 1){alcohol_list[0]} 2){alcohol_list[1]} 3){alcohol_list[2]} 4){alcohol_list[3]} 5)랜덤! 6)종료 : "))
    if alcohol == 6:
        print('다음에 또 오세요~')
        break
    elif alcohol in (1,2,3,4) :
        print(f'{alcohol_list[alcohol-1]}에 어울리는 안주는 {alcohol_foods[alcohol_list[alcohol-1]]}입니다')
        pass
    elif alcohol == 5:
        print(f'{random.choice(alcohol_list)}와 {random.choice(food_list)}는 어떠세요?')
    else:
        print('메뉴에서 골라주세요')